from __future__ import annotations

import math

from build123d import (
    Align,
    BuildPart,
    BuildSketch,
    Color,
    Cylinder,
    Mode,
    Plane,
    Polygon,
    Torus,
    extrude,
)


def external_gear_points(teeth: int, root_radius: float, outside_radius: float, phase: float = 0.0):
    points = []
    pitch = 2.0 * math.pi / teeth
    root_half = 0.47 * pitch
    top_half = 0.25 * pitch
    for tooth in range(teeth):
        center = phase + tooth * pitch
        points.extend(
            [
                (root_radius * math.cos(center - root_half), root_radius * math.sin(center - root_half)),
                (outside_radius * math.cos(center - top_half), outside_radius * math.sin(center - top_half)),
                (outside_radius * math.cos(center + top_half), outside_radius * math.sin(center + top_half)),
                (root_radius * math.cos(center + root_half), root_radius * math.sin(center + root_half)),
            ]
        )
    return points


def external_gear(
    *,
    label: str,
    teeth: int,
    root_diameter: float,
    outside_diameter: float,
    thickness: float,
    bore_diameter: float = 0.0,
    phase: float = 0.0,
    color: Color | None = None,
):
    with BuildPart() as gear:
        with BuildSketch(Plane.XY):
            Polygon(*external_gear_points(teeth, root_diameter / 2.0, outside_diameter / 2.0, phase))
        extrude(amount=thickness)
        if bore_diameter > 0.0:
            Cylinder(radius=bore_diameter / 2.0, height=thickness + 2.0, mode=Mode.SUBTRACT)
    part = gear.part
    part.label = label
    if color is not None:
        part.color = color
    return part


def cylinder_part(*, label: str, diameter: float, height: float, color: Color | None = None):
    with BuildPart() as cylinder:
        Cylinder(radius=diameter / 2.0, height=height)
    part = cylinder.part
    part.label = label
    if color is not None:
        part.color = color
    return part


def disc_with_bore(*, label: str, diameter: float, thickness: float, bore_diameter: float, color: Color):
    with BuildPart() as disc:
        Cylinder(
            radius=diameter / 2.0,
            height=thickness,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        if bore_diameter > 0.0:
            Cylinder(radius=bore_diameter / 2.0, height=thickness + 2.0, mode=Mode.SUBTRACT)
    part = disc.part
    part.label = label
    part.color = color
    return part


def orbit_track(*, label: str, radius: float, tube_radius: float, color: Color):
    with BuildPart() as ring:
        Torus(major_radius=radius, minor_radius=tube_radius)
    part = ring.part
    part.label = label
    part.color = color
    return part
