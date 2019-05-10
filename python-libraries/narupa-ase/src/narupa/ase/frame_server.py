from ase import Atoms

from . import ase_to_framedata


def ASEFrameServer(ase_atoms: Atoms, frameServer):
    def send():
        frame = ase_to_framedata(ase_atoms)
        frameServer.send_frame(send.frame_index, frame)
        send.frame_index = send.frame_index + 1

    send.frame_index = 0

    return send
