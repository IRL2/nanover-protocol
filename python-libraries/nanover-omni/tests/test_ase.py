import pytest
from ase import units, Atoms
import ase.units as ase_units
from ase.calculators.lj import LennardJones
from ase.md import VelocityVerlet

from nanover.imd import ParticleInteraction
from nanover.omni import OmniRunner
from nanover.omni.ase import ASESimulation

from common import app_server


@pytest.fixture
def example_ase(app_server, example_dynamics):
    sim = ASESimulation.from_ase_dynamics(example_dynamics)
    sim.load()
    sim.reset(app_server)
    yield sim


@pytest.fixture
def example_dynamics():
    atoms = Atoms("Ar", positions=[(0, 0, 0)], cell=[2, 2, 2])
    atoms.calc = LennardJones()
    dynamics = VelocityVerlet(atoms, timestep=0.5 * ase_units.fs)
    yield dynamics


def test_step_interval(example_ase):
    """
    Test that advancing by one step increments the dynamics steps by frame_interval.
    """
    for i in range(5):
        assert (
            example_ase.dynamics.get_number_of_steps() == i * example_ase.frame_interval
        )
        example_ase.advance_by_one_step()


def test_dynamics_interaction(example_ase):
    """
    Test that example dynamics responds to interactions.
    """
    example_ase.app_server.imd.insert_interaction(
        "interaction.0",
        ParticleInteraction(
            position=(0.0, 0.0, 10.0),
            particles=[0],
            interaction_type="constant",
        ),
    )
    for _ in range(30):
        example_ase.advance_by_one_step()

    positions = example_ase.atoms.get_positions()
    (x, y, z) = positions[0]

    # Applying a force of 1 kJ mol-1 nm-1 for
    # t = (0.5 fs * 5 simulation steps per advance * 30 advances) = 75 fs
    # using the velocity verlet algorithm should move the atom by 0.028125 nm
    # using s = u*t + 0.5*a*(t^2). Allow for numerical error with pytest.approx:
    assert z == pytest.approx(0.028125, abs=1e-8)
