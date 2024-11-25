"""
Calculate thermodynamic quantities associated with the simulation.
"""

from openmm.app import Simulation
from openmm import unit
from openmm.unit import MOLAR_GAS_CONSTANT_R


def compute_instantaneous_temperature(
    simulation: Simulation, kinetic_energy: float, dof: int
):
    r"""
    Calculate the instantaneous temperature of the system. If the integrator has an internal
    function to do this, that function is used. Otherwise, it is calculated using the
    kinetic energy of the system, according to

    .. math::
        T = \frac{2 * \mathrm{KE}}{N_{\mathrm{dof}} * R}

    where KE is the kinetic energy of the system, N_{dof} is the number of degrees of freedom
    of the system and R is the molar gas constant.

    :param simulation: OpenMM simulation of the system.
    :param kinetic_energy: Kinetic energy of the system (in kJ mol-1).
    :param dof: Number of degrees of freedom of the system.
    :return: Instantaneous temperature of the system.
    """
    KE = unit.Quantity(value=kinetic_energy, unit=unit.kilojoules_per_mole)
    integrator = simulation.context.getIntegrator()
    if hasattr(integrator, "computeSystemTemperature"):
        return integrator.computeSystemTemperature().value_in_unit(unit.kelvin)
    else:
        return (2 * KE / (dof * unit.MOLAR_GAS_CONSTANT_R)).value_in_unit(unit.kelvin)
