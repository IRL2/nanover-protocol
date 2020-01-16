import time
from typing import Generator, Tuple
from unittest.mock import Mock

import grpc
import pytest
from narupa.utilities.timing import delayed_generator
from narupa.imd.imd_client import ImdClient
from narupa.imd.imd_server import ImdServer
from narupa.imd.particle_interaction import ParticleInteraction
from narupa.protocol.imd import InteractionEndReply
from narupa.protocol.imd.imd_pb2_grpc import InteractiveMolecularDynamicsStub
from random import Random
import concurrent.futures


@pytest.fixture
def imd_server() -> Generator[ImdServer, None, None]:
    with ImdServer(address='localhost', port=0) as server:
        yield server


@pytest.fixture
def imd_server_client(imd_server) -> Generator[Tuple[ImdServer, ImdClient], None, None]:
    with ImdClient.insecure_channel(address='localhost', port=imd_server.port) as client:
        yield imd_server, client


@pytest.fixture
def imd_server_stub(imd_server) -> Generator[Tuple[ImdServer, InteractiveMolecularDynamicsStub], None, None]:
    channel = grpc.insecure_channel(f"localhost:{imd_server.port}")
    try:
        stub = InteractiveMolecularDynamicsStub(channel)
        yield imd_server, stub
    finally:
        channel.close()


@pytest.fixture
def interaction():
    return ParticleInteraction()


@pytest.fixture
def interactions_reset():
    return [ParticleInteraction(reset_velocities=True)] * 10


@pytest.fixture
def interactions():
    return [ParticleInteraction()] * 10


def test_server(imd_server):
    assert imd_server is not None


def test_publish_interaction(imd_server_stub, interaction):
    imd_server, stub = imd_server_stub
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    reply = stub.PublishInteraction((i.proto for i in [interaction]))
    assert isinstance(reply, InteractionEndReply)
    mock.callback.assert_called_once()


def test_publish_multiple_interactions(imd_server_client):
    imd_server, imd_client = imd_server_client
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    first_set = [ParticleInteraction()] * 10
    second_set = [ParticleInteraction(interaction_id="2")] * 10
    imd_client.publish_interactions_async(delayed_generator(first_set, delay=0.1))
    result = imd_client.publish_interactions(delayed_generator(second_set, delay=0.15))
    assert result is not None
    assert mock.callback.call_count == len(first_set) + len(second_set)


def test_multiplexing_interactions(imd_server_client):
    """
    The server accepts multiplexing interactions, in which different interactions
    are transmitted over the same stream. While not the typical usage, it is tested.
    """
    imd_server, imd_client = imd_server_client
    update_delay = 0.01
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    interleaved = [ParticleInteraction(interaction_id="1"), ParticleInteraction(interaction_id="2")] * 10
    # TODO use a coroutine awaiting input as the generator to control this without needing sleeps
    imd_client.publish_interactions_async(delayed_generator(interleaved, delay=update_delay))
    time.sleep(update_delay * 4)
    assert len(imd_server.service.active_interactions) == 2
    time.sleep(update_delay * (len(interleaved) + 3))
    assert mock.callback.call_count == len(interleaved)


def test_clear_interactions(imd_server_client, interactions):
    """
    Tests that after interacting the set of interactions are cleared
    """
    imd_server, imd_client = imd_server_client
    update_delay = 0.01
    update_count = len(interactions)
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    imd_client.publish_interactions_async(delayed_generator(interactions, delay=update_delay))
    time.sleep(update_delay * 4)
    assert len(imd_server.service.active_interactions) == 1
    time.sleep(update_delay * (update_count + 3))
    assert len(imd_server.service.active_interactions) == 0


def test_repeat_interactions(imd_server_client, interactions):
    imd_server, imd_client = imd_server_client
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    imd_client.publish_interactions(delayed_generator(interactions, delay=0.01))
    assert mock.callback.call_count == len(interactions)
    imd_client.publish_interactions(delayed_generator(interactions, delay=0.01))
    assert mock.callback.call_count == 2 * len(interactions)


def test_publish_identical_interactions(imd_server_client, interactions):
    """
    Tests that publishing identical interactions at the same time throws a gRPC exception.
    """
    imd_server, imd_client = imd_server_client
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    imd_client.publish_interactions_async(delayed_generator(interactions, delay=0.1))
    with pytest.raises(grpc.RpcError):
        imd_client.publish_interactions(delayed_generator(interactions, delay=0.15))


def test_publish_interactive_interaction(imd_server_client, interactions):
    """
    Tests that we can publish interactions using interactive generator.
    """
    imd_server, imd_client = imd_server_client
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)
    guid = imd_client.start_interaction()
    for interaction in interactions:
        imd_client.update_interaction(guid, interaction)
    imd_client.stop_interaction(guid)
    time.sleep(0.05)
    assert mock.callback.call_count == len(interactions)


@pytest.mark.timeout(20)
def test_multithreaded_interactions(imd_server_client):
    """
    Test that starting, stopping and accessing interactions in a multithreaded
    scenario does not throw any exceptions or deadlock.
    If access to the interactions were not thread safe, it would throw an exception.
    """
    imd_server, imd_client = imd_server_client

    number_of_runs = 20
    interactions_per_run = 10
    random = Random()
    mock = Mock()
    imd_server.service.set_interaction_updated_callback(mock.callback)

    # runs an interaction on the threadpool.
    def run_interaction(imd_client: ImdClient, interaction_id, num_interactions):
        interactions = [ParticleInteraction(interaction_id=str(interaction_id))] * num_interactions
        delay = random.uniform(0.0001, 0.1)
        return imd_client.publish_interactions_async(delayed_generator(interactions, delay=delay))

    # run lots of interactions that constantly change the interactions dictionary size.
    interaction_tasks = {run_interaction(imd_client, i, interactions_per_run) for i in range(number_of_runs)}
    # TODO - add a long running interaction so there is always some interaction to fetch

    # access the interactions, while other tasks are still running.
    for _ in concurrent.futures.as_completed(interaction_tasks):
        for interaction in imd_server.service.active_interactions.values():
            # sleep while iterating over the interactions. If access is not threadsafe, this will cause a
            # RuntimeError.
            time.sleep(0.01)
            assert isinstance(interaction, ParticleInteraction)

    # check that the callback has been called the correct number of times
    assert mock.callback.call_count == interactions_per_run * number_of_runs


def test_velocity_reset_not_enabled(imd_server_client, interactions_reset):
    imd_server, imd_client = imd_server_client
    with pytest.raises(grpc.RpcError):
        imd_client.publish_interactions(delayed_generator(interactions_reset, delay=0.1))


def test_velocity_reset_enabled(imd_server_client, interactions_reset):
    imd_server, imd_client = imd_server_client
    imd_server.service.velocity_reset_enabled = True
    imd_client.publish_interactions(delayed_generator(interactions_reset, delay=0.1))


def test_particle_range_max(imd_server_client, interaction):
    imd_server, imd_client = imd_server_client
    imd_server.service.number_of_particles = 5
    interaction.particles = [1, 2, 3, 4, 5, 6]
    with pytest.raises(grpc.RpcError):
        imd_client.publish_interactions([interaction])


def test_particle_range_particles_not_set(imd_server_client, interaction):
    """
    Tests that if the number of particles is not set in the imd service, it will not
    report error if particle out of range.
    """
    imd_server, imd_client = imd_server_client
    interaction.particles = [1, 2, 3, 4, 5, 6]
    imd_client.publish_interactions([interaction])

def test_particle_range_particles_not_set(imd_server_client, interaction):
    """
    Tests that if the number of particles is not set in the imd service, it will not
    report error if particle out of range.
    """
    imd_server, imd_client = imd_server_client
    interaction.particles = [1, 2, 3, 4, 5, 6]
    imd_client.publish_interactions([interaction])