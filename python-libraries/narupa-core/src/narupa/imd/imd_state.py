# Copyright (c) Intangible Realities Lab, University Of Bristol. All rights reserved.
# Licensed under the GPL. See License.txt in the project root for license information.
"""
Module providing methods for storing ParticleInteractions in a StateDictionary.
"""
from typing import Dict, Any

from narupa.state.state_dictionary import StateDictionary
from narupa.utilities.change_buffers import DictionaryChange
from narupa.imd.particle_interaction import ParticleInteraction

IMD_SERVICE_NAME = "imd"
INTERACTION_PREFIX = 'interaction.'
VELOCITY_RESET_KEY = 'imd.velocity_reset_enabled'


class ImdStateWrapper:
    """
    A wrapper around a StateDictionary that provides convenient methods for
    accessing and modifying ParticleInteractions.

    :param state_dictionary: The state dictionary to wrap.
    :param velocity_reset_enabled: Whether the dynamics this service is being
        used in supports velocity reset.
    """

    def __init__(
            self,
            state_dictionary: StateDictionary,
            velocity_reset_enabled=False,
    ):
        self.state_dictionary = state_dictionary
        self.velocity_reset_enabled = velocity_reset_enabled

        self.state_dictionary.update_locks(
            self,
            acquire={VELOCITY_RESET_KEY: None},
        )
        self.state_dictionary.update_state(
            self,
            change=DictionaryChange(updates={
                VELOCITY_RESET_KEY: velocity_reset_enabled
            }),
        )

    @property
    def velocity_reset_enabled(self):
        with self.state_dictionary.lock_content() as state:
            return state[VELOCITY_RESET_KEY]

    @velocity_reset_enabled.setter
    def velocity_reset_enabled(self, value: bool):
        change = DictionaryChange(updates={VELOCITY_RESET_KEY: value})
        self.state_dictionary.update_state(self, change)

    def insert_interaction(self, interaction_id: str, interaction: ParticleInteraction):
        assert interaction_id.startswith(INTERACTION_PREFIX)
        change = DictionaryChange(updates={
            interaction_id: interaction_to_dict(interaction),
        })
        self.state_dictionary.update_state(None, change)

    def remove_interaction(self, interaction_id: str):
        assert interaction_id.startswith(INTERACTION_PREFIX)
        change = DictionaryChange(removals=[interaction_id])
        self.state_dictionary.update_state(None, change)

    @property
    def active_interactions(self) -> Dict[str, ParticleInteraction]:
        """
        The current dictionary of active interactions, keyed by interaction id.

        :return: A copy of the dictionary of active interactions.
        """
        return {
            key: dict_to_interaction(value)
            for key, value in self.state_dictionary.copy_content().items()
            if key.startswith(INTERACTION_PREFIX)
        }


def interaction_to_dict(interaction: ParticleInteraction):
    try:
        dictionary = {
            "position": [float(f) for f in interaction.position],
            "particles": [int(i) for i in interaction.particles],
            "interaction_type": interaction.type,
            "scale": interaction.scale,
            "mass_weighted": interaction.mass_weighted,
            "reset_velocities": interaction.reset_velocities,
            "max_force": interaction.max_force,
        }
        dictionary.update(interaction.properties)
        return dictionary
    except AttributeError as e:
        raise TypeError from e


def dict_to_interaction(dictionary: Dict[str, Any]) -> ParticleInteraction:
    kwargs = dict(**dictionary)
    kwargs['particles'] = [int(i) for i in kwargs['particles']]
    return ParticleInteraction(**kwargs)
