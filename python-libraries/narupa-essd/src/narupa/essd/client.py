# Copyright (c) Intangible Realities Lab, University Of Bristol. All rights reserved.
# Licensed under the GPL. See License.txt in the project root for license information.
"""
A module containing a Extremely Simple Service Discovery client.
"""
import json
import socket
import time
from typing import Optional

import select

from narupa.essd.server import BROADCAST_PORT, _connect_socket
from narupa.essd.servicehub import ServiceHub, MAXIMUM_MESSAGE_SIZE
from narupa.essd.utils import yield_interval

IP_ADDRESS_ANY = "0.0.0.0"


class DiscoveryClient:

    def __init__(self, address: Optional[str] = None, port: Optional[int] = None):
        if address is None:
            address = IP_ADDRESS_ANY
        if port is None:
            port = BROADCAST_PORT
        self.address = address
        self.port = port
        self._connect()

    def _connect(self):
        self._socket = _connect_socket()
        self._socket.bind((self.address, self.port))

    def _check_for_messages(self):
        socket_list = [self._socket]
        readable, _, exceptional = select.select(socket_list, [], socket_list)
        if len(exceptional) > 0:
            raise ConnectionError("Exception on socket while checking for messages.")
        return len(readable) > 0

    def _receive_service(self):
        (message, address) = self._socket.recvfrom(MAXIMUM_MESSAGE_SIZE)
        properties = json.loads(message.decode())
        return ServiceHub(**properties)

    def search_for_services(self, search_time: float = 5.0, interval=0.033):
        """
        Searches for services for the given amount of time, blocking.
        :param search_time: Time, in seconds, to search for.
        :return: A set of services discovered over the duration.

        The returned set of services are all those that were found during searching. They may not
        still exist by the end of the search.

        """
        total_time = 0
        services = set()
        previous_time = time.monotonic()
        for _ in yield_interval(interval):
            new_time = time.monotonic()
            total_time += new_time - previous_time
            previous_time = new_time
            if total_time > search_time:
                return services
            if self._check_for_messages():
                service = self._receive_service()
                if service is not None:
                    services.add(service)

    def close(self):
        self._socket.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
