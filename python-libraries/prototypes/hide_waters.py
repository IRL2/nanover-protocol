from nanover.app import NanoverImdClient

WATER_RESIDUE_NAME = "HOH"

with NanoverImdClient.autoconnect() as client:
    client.subscribe_to_frames()
    client.subscribe_multiplayer()
    first_frame = client.wait_until_first_frame(check_interval=0.5, timeout=10)

    print(f"Attempting to hide residue {WATER_RESIDUE_NAME} (residues in frame: {', '.join(set(first_frame.residue_names))})")

    waters = (
        particle_index 
        for particle_index, residue_index 
        in enumerate(first_frame.particle_residues) 
        if first_frame.residue_names[residue_index] == WATER_RESIDUE_NAME
    )

    water = client.create_selection("water", waters)
    water.hide = True
    water.flush_changes()
