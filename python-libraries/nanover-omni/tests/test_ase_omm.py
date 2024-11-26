import warnings

import pytest
from ase import units

from nanover.ase.wall_constraint import VelocityWallConstraint
from nanover.omni.ase_omm import ASEOpenMMSimulation, CONSTRAINTS_UNSUPPORTED_MESSAGE

from common import make_app_server, ARGON_XML_PATH
from nanover.openmm.serializer import deserialize_simulation


from openmm_simulation_utils import (
    build_single_atom_simulation,
    build_basic_simulation,
)


@pytest.fixture
def example_ase_omm():
    with make_app_server() as app_server:
        sim = ASEOpenMMSimulation.from_simulation(build_single_atom_simulation())
        sim.load()
        sim.reset(app_server)
        yield sim


def test_step_interval(example_ase_omm):
    """
    Test that advancing by one step increments the dynamics steps by frame_interval.
    """
    for i in range(5):
        assert (
            example_ase_omm.dynamics.get_number_of_steps()
            == i * example_ase_omm.frame_interval
        )
        example_ase_omm.advance_by_one_step()


# TODO: test it actually outputs
def test_verbose(example_ase_omm):
    """
    Test verbose option steps without exceptions.
    """
    with make_app_server() as app_server:
        example_ase_omm.verbose = True
        example_ase_omm.reset(app_server)
        for i in range(5):
            example_ase_omm.advance_by_one_step()


@pytest.mark.parametrize("walls", (False, True))
def test_walls(example_ase_omm, walls):
    example_ase_omm.use_walls = walls
    example_ase_omm.load()
    assert (
        any(
            isinstance(constraint, VelocityWallConstraint)
            for constraint in example_ase_omm.atoms.constraints
        )
        == walls
    )


def test_no_constraint_no_warning(example_ase_omm):
    """
    Test that a system without constraints does not cause a constraint warning
    to be logged.
    """
    with make_app_server() as app_server:
        with warnings.catch_warnings():
            warnings.simplefilter("error", UserWarning)
            example_ase_omm.load()
            example_ase_omm.reset(app_server)


def test_constraint_warning(example_ase_omm, recwarn):
    """
    Test that a system with constraints causes a constraint warning to be
    logged.
    """
    with make_app_server() as app_server:
        with pytest.warns(UserWarning, match=CONSTRAINTS_UNSUPPORTED_MESSAGE):
            example_ase_omm.simulation.system.addConstraint(0, 1, 1)
            example_ase_omm.load()
            example_ase_omm.reset(app_server)
