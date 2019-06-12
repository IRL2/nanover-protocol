# Copyright (c) Intangible Realities Lab, University Of Bristol. All rights reserved.
# Licensed under the GPL. See License.txt in the project root for license information.
import logging
import time
from concurrent import futures
from concurrent.futures import Future
from queue import Queue
from typing import Iterable, Optional

import grpc
from narupa.imd.imd_server import DEFAULT_ADDRESS, DEFAULT_PORT
from narupa.imd.interaction import Interaction
from narupa.protocol.imd import InteractiveMolecularDynamicsStub, InteractionEndReply


def delayed_generator(iterable: Iterable, delay: float = 0):
    """
    Turns an iterable collection into a generator, where each item is yielded after the given delay (seconds).
    :param iterable: Iterable collection of items to be yielded.
    :param delay: delay (seconds) to wait until yielding the next item in the collection.
    :return:
    """
    for item in iterable:
        time.sleep(delay)
        yield item


def queue_generator(queue: Queue, sentinel: object):
    """
    Produces a generator that can be used to iterate over the values submitted to a queue, until the
    given sentinel is added to the queue. The iterator will block until this sentinel is passed.

    Enables one to take control of when items are passed to a streaming iterator, such as that used
    in :method: publish_interactions_async.

    :param queue: Queue that items will be submitted to.
    :param sentinel: A sentinel that indicates the end of iteration. When added to the queue,
                     the generator stops.
    :return: Yields the items in put into the queue, in the order they were put in.

    Example
    -------

    .. code python

    queue = Queue()
    sentinel = object()

    queue.put(1)
    queue.put(2)
    queue.put(sentinel)

    generator = queue_generator(queue, sentinel)
    for item in generator:
        print(item)

    """
    for val in iter(queue.get, sentinel):
        yield val


def _to_proto(interactions: Iterable[Interaction]):
    for interaction in interactions:
        yield interaction.proto


class ImdClient:
    """
    A simple IMD client, primarily for testing the IMD server.
    """

    def __init__(self, *, address: Optional[str] = None, port: Optional[int] = None):
        if address is None:
            address = DEFAULT_ADDRESS
        if port is None:
            port = DEFAULT_PORT
        self.channel = grpc.insecure_channel("{0}:{1}".format(address, port))
        self.stub = InteractiveMolecularDynamicsStub(self.channel)
        self.threads = futures.ThreadPoolExecutor(max_workers=10)
        self._active_interactions = {}
        self._logger = logging.getLogger(__name__)

    def start_interaction(self) -> int:
        """
        Start an interaction
        :return: A unique identifier to be used to update the interaction.
        """
        queue = Queue()
        sentinel = object()
        future = self.publish_interactions_async(queue_generator(queue, sentinel))
        if len(self._active_interactions) == 0:
            interaction_id = 0
        else:
            interaction_id = max(self._active_interactions) + 1
        self._active_interactions[interaction_id] = (queue, sentinel, future)
        return interaction_id

    def update_interaction(self, interaction_id, interaction: Interaction):
        """
        Update the interaction given by the interaction_id with an updated instance of an
        interaction. Typically used to adjust the position of an interaction over time.
        """
        if interaction_id not in self._active_interactions:
            raise KeyError("Attempted to update an interaction with an unknown interaction ID.")
        queue, _, _ = self._active_interactions[interaction_id]
        queue.put(interaction)

    def stop_interaction(self, interaction_id) -> InteractionEndReply:
        """
        Stop the interaction determined by the given ID.
        """
        if interaction_id not in self._active_interactions:
            raise KeyError("Attempted to stop an interaction with an unknown interaction ID.")
        queue, sentinel, future = self._active_interactions[interaction_id]
        queue.put(sentinel)
        del self._active_interactions[interaction_id]
        return future.result()

    def publish_interactions_async(self, interactions: Iterable[Interaction]) -> Future:
        """
        Publishes the iterable of interactions on a thread.
        :param interactions: An iterable generator or collection of interactions.
        :return Future representing the state of the interaction task.
        """
        return self.threads.submit(self.publish_interactions, interactions)

    def publish_interactions(self, interactions: Iterable[Interaction]) -> InteractionEndReply:
        """
        Publishes the generator of interactions on a thread.
        :param interactions: An iterable generator or collection of interactions.
        :return: A reply indicating successful publishing of interaction.
        """
        return self.stub.PublishInteraction(_to_proto(interactions))

    def stop_all_interactions(self):
        """
        Stops all active interactions governed by this client.
        """
        for interaction_id in list(self._active_interactions.keys()):
            self.stop_interaction(interaction_id)

    def close(self):
        try:
            pass
            #self.stop_all_interactions()
        except grpc.RpcError as e:
            self._logger.exception(e)
        finally:
            self.channel.close()
            self.threads.shutdown(wait=False)
