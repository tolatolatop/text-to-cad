from build123d import Color, Compound, Location

from orrery_base_components import cylinder_part, disc_with_bore, external_gear, orbit_track


def placed(shape, name: str, x: float, y: float, z: float):
    part = shape.located(Location((x, y, z)))
    part.label = name
    return part


def gen_step():
    earth_drive_center_x = 90.0
    moon_input_x = -72.0
    moon_idler_x = -42.0
    moon_output_x = -17.0
    moon_train_y = -58.0

    children = [
        placed(
            disc_with_bore(
                label="round_display_base_plate_d220",
                diameter=220.0,
                thickness=5.0,
                bore_diameter=18.0,
                color=Color(0.13, 0.15, 0.18),
            ),
            "base_plate",
            0.0,
            0.0,
            -5.0,
        ),
        placed(
            orbit_track(
                label="engraved_earth_orbit_reference_track",
                radius=78.0,
                tube_radius=0.75,
                color=Color(0.50, 0.55, 0.60),
            ),
            "earth_orbit_reference_track",
            0.0,
            0.0,
            1.2,
        ),
        placed(
            external_gear(
                label="large_earth_orbit_turntable_gear_96t",
                teeth=96,
                root_diameter=138.0,
                outside_diameter=152.0,
                thickness=7.0,
                bore_diameter=58.0,
                phase=0.02618,
                color=Color(0.35, 0.52, 0.65),
            ),
            "earth_orbit_turntable_gear",
            0.0,
            0.0,
            2.0,
        ),
        placed(
            cylinder_part(
                label="fixed_center_sun_axis_hub_no_ball",
                diameter=24.0,
                height=13.0,
                color=Color(0.86, 0.58, 0.17),
            ),
            "fixed_center_sun_axis_hub",
            0.0,
            0.0,
            3.5,
        ),
        placed(
            external_gear(
                label="earth_orbit_drive_pinion_24t",
                teeth=24,
                root_diameter=32.0,
                outside_diameter=42.0,
                thickness=7.0,
                bore_diameter=6.0,
                phase=0.05236,
                color=Color(0.90, 0.64, 0.20),
            ),
            "earth_drive_pinion",
            earth_drive_center_x,
            0.0,
            2.0,
        ),
        placed(
            cylinder_part(
                label="drive_or_locator_pin",
                diameter=5.6,
                height=14.0,
                color=Color(0.82, 0.84, 0.80),
            ),
            "earth_drive_pinion_pin",
            earth_drive_center_x,
            0.0,
            4.0,
        ),
        placed(
            disc_with_bore(
                label="raised_moon_train_mounting_pad",
                diameter=90.0,
                thickness=2.0,
                bore_diameter=1.0,
                color=Color(0.22, 0.25, 0.28),
            ),
            "moon_train_mounting_pad",
            -36.0,
            -58.0,
            8.5,
        ),
        placed(
            external_gear(
                label="moon_reduction_gear_18t",
                teeth=18,
                root_diameter=26.0,
                outside_diameter=36.0,
                thickness=5.0,
                bore_diameter=4.0,
                phase=0.08727,
                color=Color(0.74, 0.74, 0.68),
            ),
            "moon_input_gear",
            moon_input_x,
            moon_train_y,
            11.0,
        ),
        placed(
            cylinder_part(
                label="drive_or_locator_pin",
                diameter=5.6,
                height=14.0,
                color=Color(0.82, 0.84, 0.80),
            ),
            "moon_input_gear_pin",
            moon_input_x,
            moon_train_y,
            12.0,
        ),
        placed(
            external_gear(
                label="moon_reduction_gear_18t",
                teeth=18,
                root_diameter=26.0,
                outside_diameter=36.0,
                thickness=5.0,
                bore_diameter=4.0,
                phase=0.17453,
                color=Color(0.62, 0.66, 0.70),
            ),
            "moon_idler_gear",
            moon_idler_x,
            moon_train_y,
            11.0,
        ),
        placed(
            cylinder_part(
                label="drive_or_locator_pin",
                diameter=5.6,
                height=14.0,
                color=Color(0.82, 0.84, 0.80),
            ),
            "moon_idler_gear_pin",
            moon_idler_x,
            moon_train_y,
            12.0,
        ),
        placed(
            external_gear(
                label="moon_output_gear_12t",
                teeth=12,
                root_diameter=18.0,
                outside_diameter=27.0,
                thickness=5.0,
                bore_diameter=3.2,
                phase=0.26180,
                color=Color(0.74, 0.74, 0.68),
            ),
            "moon_output_gear",
            moon_output_x,
            moon_train_y,
            11.0,
        ),
        placed(
            cylinder_part(
                label="drive_or_locator_pin",
                diameter=5.6,
                height=14.0,
                color=Color(0.82, 0.84, 0.80),
            ),
            "moon_output_gear_pin",
            moon_output_x,
            moon_train_y,
            12.0,
        ),
    ]
    return {"shape": Compound(children=children, label="orrery_sun_earth_moon")}
