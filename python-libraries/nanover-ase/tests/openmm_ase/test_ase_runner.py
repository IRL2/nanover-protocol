import os
from logging import Handler, WARNING
import time

import numpy
import pytest
from ase import units
from nanover.app.app_server import DEFAULT_NANOVER_PORT
from nanover.app import NanoverImdClient
from ase.io import read
from nanover.ase.openmm import ASEOpenMMRunner
from nanover.ase.openmm.runner import (
    ImdParams,
    CONSTRAINTS_UNSUPPORTED_MESSAGE,
    LoggingParams,
)
from nanover.core import DEFAULT_SERVE_ADDRESS
from nanover.essd import DiscoveryClient
from nanover.ase.openmm.calculator import OpenMMCalculator
from nanover.ase.wall_constraint import VelocityWallConstraint

from .simulation_utils import basic_simulation, serialized_simulation_path

TRAJECTORY_OUTPUT_FILENAME = "test.xyz"
TIMING_TOLERANCE = 0.007  # 7ms


class ListLogHandler(Handler):
    """
    Records records from a logger into a list that can be examined for testing.
    """

    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)

    def count_records(self, message: str, levelno: int):
        return sum(
            1
            for record in self.records
            if record.message == message and record.levelno == levelno
        )


@pytest.fixture()
def imd_params():
    """
    Test ImdParams set to use any available port, to avoid port clashes between tests.
    """
    params = ImdParams(port=0)
    return params


@pytest.fixture()
def logging_params(tmp_path):
    params = LoggingParams(
        trajectory_file=os.path.join(tmp_path, TRAJECTORY_OUTPUT_FILENAME),
        write_interval=1,
    )
    return params


@pytest.fixture()
def runner(basic_simulation, imd_params):
    with ASEOpenMMRunner(basic_simulation, imd_params=imd_params) as runner:
        yield runner


@pytest.fixture()
def client_runner(runner):
    with NanoverImdClient.connect_to_single_server(port=runner.port) as client:
        yield client, runner


@pytest.fixture()
def default_runner(basic_simulation):
    with ASEOpenMMRunner(basic_simulation) as runner:
        yield runner


def test_from_xml(serialized_simulation_path, imd_params):
    with ASEOpenMMRunner.from_xml(
        serialized_simulation_path, params=imd_params
    ) as runner:
        assert runner.simulation is not None


def test_from_xmls(serialized_simulation_path, imd_params):
    with ASEOpenMMRunner.from_xmls(
        [serialized_simulation_path], params=imd_params
    ) as runner:
        assert len(runner.simulation_list) > 0


def test_list_simulations(client_runner):
    client, runner = client_runner
    assert len(client.run_list()) > 0


def test_next_simulation(client_runner):
    client, runner = client_runner
    runner.play()
    client.subscribe_to_frames()
    client.wait_until_first_frame()
    assert client.current_frame.simulation_counter == 0
    client.run_next()
    time.sleep(0.5)
    assert client.current_frame.simulation_counter == 1


@pytest.mark.serial
def test_defaults(default_runner):
    runner = default_runner
    default_params = ImdParams()
    assert runner.verbose == default_params.verbose
    assert runner.frame_interval == default_params.frame_interval
    assert runner.time_step == default_params.time_step
    assert runner.port == DEFAULT_NANOVER_PORT
    assert runner.address == DEFAULT_SERVE_ADDRESS


def test_dynamics_initialised(runner):
    assert runner.dynamics is not None


def test_run(runner):
    runner.run(10)
    assert runner.dynamics.get_number_of_steps() == 10


def test_frames_sent(runner):
    """
    Test that the frame server has received frames after running dynamics.
    """
    runner.run(12)
    assert runner.app_server.frame_publisher.last_frame_index > 0


def test_verbose(basic_simulation, imd_params):
    imd_params.verbose = True
    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        runner.run(10)


@pytest.mark.parametrize("interval", (1, 2, 3))
def test_frame_interval(basic_simulation, interval, imd_params):
    """
    Test that the frame server receives frames at the correct interval of
    dynamics steps.
    """
    imd_params.frame_interval = interval
    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        runner.run(1)
        prev = runner.app_server.frame_publisher.last_frame_index
        runner.run(interval * 3)
        assert runner.app_server.frame_publisher.last_frame_index == prev + 3


def test_time_step(basic_simulation, imd_params):
    imd_params.time_step = 0.5
    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        assert runner.dynamics.dt == pytest.approx(0.5 * units.fs)


@pytest.mark.parametrize(
    "walls",
    (
        False,
        True,
    ),
)
def test_walls(basic_simulation, walls, imd_params):
    imd_params.walls = walls

    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        assert (
            any(
                isinstance(constraint, VelocityWallConstraint)
                for constraint in runner.atoms.constraints
            )
            == walls
        )


def test_no_constraint_no_warning(basic_simulation, imd_params):
    """
    Test that a system without constraints does not cause a constraint warning
    to be logged.
    """
    handler = ListLogHandler()

    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        runner._logger.addHandler(handler)
        runner._validate_simulation()
        assert handler.count_records(CONSTRAINTS_UNSUPPORTED_MESSAGE, WARNING) == 0


def test_constraint_warning(basic_simulation, imd_params):
    """
    Test that a system with constraints causes a constraint warning to be
    logged.
    """
    handler = ListLogHandler()
    basic_simulation.system.addConstraint(0, 1, 1)

    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        runner._logger.addHandler(handler)
        runner._validate_simulation()
        assert handler.count_records(CONSTRAINTS_UNSUPPORTED_MESSAGE, WARNING) == 1


def test_no_discovery(basic_simulation, imd_params):
    imd_params.discovery = False
    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        assert not runner.running_discovery


@pytest.mark.serial
def test_discovery(basic_simulation, imd_params):
    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        assert runner.running_discovery
        assert runner.app_server.discovery is not None
        assert len(runner.app_server.discovery.services) == 1


@pytest.mark.serial
def test_discovery_with_client(basic_simulation, imd_params):
    imd_params.name = "ASE Test Runner"
    with ASEOpenMMRunner(basic_simulation, imd_params) as runner:
        assert runner.running_discovery
        discovery = runner.app_server.discovery
        assert len(discovery.services) == 1
        with DiscoveryClient() as client:
            # There may be servers running already, we only want to look at the
            # one we created in that test. We select it by name.
            servers = set(client.search_for_services(search_time=0.8, interval=0.01))
            relevant_servers = [
                server for server in servers if server.name == imd_params.name
            ]
            assert len(relevant_servers) == 1
            server = relevant_servers[0]
            assert server in discovery.services
            assert server.name == runner.name
            assert len(server.services) == 3
            for port in server.services.values():
                assert port == runner.app_server.port


def test_logging(basic_simulation, imd_params, logging_params):
    with ASEOpenMMRunner(basic_simulation, imd_params, logging_params) as runner:
        runner.run(1)

    trajectory_file = runner.logging_info.trajectory_path
    assert os.path.exists(trajectory_file)
    assert runner.logging_info.base_trajectory_path == logging_params.trajectory_file

    atom_images = read(trajectory_file, index=":")
    assert len(atom_images) == 2


def test_no_logging(runner):
    assert runner.logging_info is None


def test_logging_rate(basic_simulation, imd_params, logging_params):
    logging_params.write_interval = 10
    expected_frames = 3

    with ASEOpenMMRunner(basic_simulation, imd_params, logging_params) as runner:
        runner.run(expected_frames * logging_params.write_interval)

    trajectory_file = runner.logging_info.trajectory_path
    assert os.path.exists(trajectory_file)

    atom_images = read(trajectory_file, index=":")
    # always get one more frame as it dumps out the initial frame
    assert len(atom_images) == expected_frames + 1


def test_get_dynamics_interval(runner):
    assert runner.dynamics_interval == runner.imd._variable_interval_generator.interval


def test_set_dynamics_interval(runner):
    value = 0.2
    runner.dynamics_interval = value
    assert runner.dynamics_interval == pytest.approx(value)


@pytest.mark.serial
@pytest.mark.parametrize("fps", (5, 10, 30))
def test_throttling(client_runner, fps):
    """
    The runner uses the requested MD throttling.

    Here we make sure the runner throttles the dynamics according to the
    dynamics interval. However, we only guarantee that the target dynamics
    interval is close on average.
    """
    # We need at least a few frames to see intervals between
    test_frames = 30

    dynamics_interval = 1 / fps
    client, runner = client_runner
    runner.dynamics_interval = dynamics_interval

    client.subscribe_to_all_frames()
    runner.run()

    while len(client.frames) < test_frames:
        time.sleep(0.1)

    runner.imd.cancel_run(wait=True)

    # first frame (topology) isn't subject to intervals
    timestamps = [frame.server_timestamp for frame in client.frames[1:]]
    deltas = numpy.diff(timestamps)

    # The interval is not very accurate. We only check that the observed
    # interval is close on average.
    assert numpy.average(deltas) == pytest.approx(
        dynamics_interval, abs=TIMING_TOLERANCE
    )
