from os import PathLike
from pathlib import Path
from typing import Optional, Any

from openmm.app import Simulation, StateDataReporter

from nanover.app import NanoverImdApplication
from nanover.imd import ParticleInteraction
from nanover.openmm import serializer, openmm_to_frame_data
from nanover.openmm.imd import (
    create_imd_force,
    NanoverImdReporter,
    add_imd_force_to_system, get_sparse_forces,
)


class OpenMMSimulation:
    @classmethod
    def from_simulation(cls, simulation: Simulation, *, name: Optional[str] = None):
        sim = cls(name)
        sim.simulation = simulation
        sim.imd_force = add_imd_force_to_system(simulation.system)
        sim.simulation.context.reinitialize(preserveState=True)

        sim.checkpoint = sim.simulation.context.createCheckpoint()

        return sim

    @classmethod
    def from_xml_path(cls, path: PathLike[str], *, name: Optional[str] = None):
        sim = cls(name or Path(path).stem)
        sim.xml_path = path
        return sim

    def __init__(self, name: Optional[str] = None):
        self.name = name or "Unnamed OpenMM Simulation"

        self.xml_path: Optional[PathLike[str]] = None
        self.app_server: Optional[NanoverImdApplication] = None

        self.frame_interval = 5
        self.force_interval = 5
        self.include_velocities = False
        self.include_forces = False
        self.platform: Optional[str] = None

        self._frame_index = 1

        self.imd_force = create_imd_force()
        self.simulation: Optional[Simulation] = None
        self.checkpoint: Optional[Any] = None
        self.reporter: Optional[NanoverImdReporter] = None
        self.verbose_reporter: Optional[StateDataReporter] = None

    def load(self):
        if self.xml_path is None or self.simulation is not None:
            return

        with open(self.xml_path) as infile:
            self.imd_force = create_imd_force()
            self.simulation = serializer.deserialize_simulation(
                infile, imd_force=self.imd_force, platform_name=self.platform
            )

        self.checkpoint = self.simulation.context.createCheckpoint()

    def reset(self, app_server: NanoverImdApplication):
        assert self.simulation is not None and self.checkpoint is not None

        self.app_server = app_server
        self.simulation.context.loadCheckpoint(self.checkpoint)

        try:
            self.simulation.reporters.remove(self.reporter)
            if self.verbose_reporter is not None:
                self.simulation.reporters.remove(self.verbose_reporter)
        except ValueError:
            pass

        self.reporter = NanoverImdReporter(
            frame_interval=self.frame_interval,
            force_interval=self.force_interval,
            include_velocities=self.include_velocities,
            include_forces=self.include_forces,
            imd_force=self.imd_force,
            imd_state=self.app_server.imd,
            frame_publisher=self.app_server.frame_publisher,
        )
        self.simulation.reporters.append(self.reporter)
        if self.verbose_reporter is not None:
            self.simulation.reporters.append(self.verbose_reporter)

        self.app_server.imd.insert_interaction("interaction.ass", ParticleInteraction(particles=[0], scale=100))

    def advance_to_next_report(self):
        assert self.simulation is not None
        self.simulation.step(self.frame_interval)
        print(f"{self.test_potential_energy()}")

    def advance_by_seconds(self, dt: float):
        self.advance_to_next_report()

    def advance_by_one_step(self):
        self.advance_to_next_report()

    def test_potential_energy(self):
        state1 = self.simulation.context.getState(getEnergy=True, groups=-1)
        state2 = self.simulation.context.getState(getEnergy=True, groups=1)

        return state1.getPotentialEnergy(), state2.getPotentialEnergy()

    def report_frame(self):
        pass
        # state = self.simulation.context.getState()
        #
        # if not self._did_first_frame:
        #     self._did_first_frame = True
        #     self._on_first_frame(simulation)
        #
        # interactions = self.app_server.imd.active_interactions
        # positions = state.getPositions(asNumpy=True)
        # total_user_energy, user_forces = self.update_forces(
        #     positions.astype(float), interactions, self.simulation.context
        # )
        #
        # frame_data = openmm_to_frame_data(
        #     state=state,
        #     topology=None,
        #     include_positions=False,
        #     include_velocities=self.include_velocities,
        #     include_forces=self.include_forces,
        # )
        #
        # frame_data.particle_positions = positions
        # frame_data.user_energy = total_user_energy
        # sparse_indices, sparse_forces = get_sparse_forces(self.user_forces)
        # frame_data.user_forces_sparse = sparse_forces
        # frame_data.user_forces_index = sparse_indices
        # self.app_server.frame_publisher.send_frame(self._frame_index, frame_data)
        # self._frame_index += 1
