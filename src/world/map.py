from locations.location import Location


lermwick_prison_hallway = Location(
    "Lermwick Prison Hallway",
    [],
    [],
    []
)

lermwick_prison_cell = Location(
    "Lermwick Prison",
    [],
    [],
    []
)
lermwick_prison_cell.entrances.append(lermwick_prison_hallway)