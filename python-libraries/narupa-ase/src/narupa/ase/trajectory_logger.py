from typing import Optional

import ase.io
from ase import Atoms


class TrajectoryLogger:
    """
    Trajectory logging class for use with ASE simulations.

    :param atoms: ASE :class:`Atoms` from which to write data.
    :param filename: Path to filename to write to.
    :param format: Format to use, as supported by ASE. If not specified, derived from filename.
    :param parallel: 
    :param kwargs:
    """

    def __init__(self, atoms: Atoms, filename: str, format: Optional[str] = None, parallel=True, **kwargs):
        """


        """
        self.frame_index = 0
        self.atoms = atoms
        self.filename = filename
        self.format = format
        self.parallel = parallel
        self._kwargs = kwargs

    def write(self):
        should_append = self.frame_index != 0
        ase.io.write(self.filename,
                     self.atoms,
                     format=self.format,
                     parallel=self.parallel,
                     append=should_append,
                     **self._kwargs)

    def __call__(self):
        self.write()
