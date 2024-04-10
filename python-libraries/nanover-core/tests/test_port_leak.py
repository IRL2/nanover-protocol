import os
import socket
import pytest
from nanover.app.app_server import DEFAULT_NANOVER_PORT

trigger = os.environ.get("NANOVER_PORT_LEAK")
if trigger in ("pass", "fail"):

    @pytest.fixture
    def leaking_default_port():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", DEFAULT_NANOVER_PORT))

    def test_leak_default_port(leaking_default_port):
        """
        Open the default port and let it open on purpose.

        This test allows to test hypotheses about the default port leaking.
        """
        assert trigger == "pass"
