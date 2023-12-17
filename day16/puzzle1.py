

# tile: (type, energized), where engergized is a bitmap indicating directions that light has entered the tile

from typing import Final, TypedDict

Beam = tuple[tuple[int, int], tuple[int, int]] # ((start_x, start_y), (delta_x, delta_y))

class Tile(TypedDict):
    type: str
    energized: int # bit field

Contraption = list[list[Tile]]

FROM_NORTH: Final = 1
FROM_SOUTH: Final = 2
FROM_EAST: Final = 4
FROM_WEST: Final = 8

DIRECTION_MAP: Final[dict[tuple[int, int], int]] = {
    (0, 1): FROM_NORTH,
    (0, -1): FROM_SOUTH,
    (1, 0): FROM_WEST,
    (-1, 0): FROM_EAST
}

def walk_beam_path(contraption: Contraption, beam: Beam ) -> list[Beam]:
    beams: list[Beam] = []

    pos_x, pos_y = beam[0]

    while (pos_y in range(0, len(contraption))) and (pos_x in range(0, len(contraption[pos_y]))):

        from_direction = DIRECTION_MAP[beam[1]]

        tile = contraption[pos_y][pos_x]

        if tile['energized'] & from_direction:
            # a beam already came from this direction. Ignore the beam
            break

        tile['energized'] |= from_direction

        match tile['type']:
            case '|':
                if from_direction in (FROM_EAST, FROM_WEST):
                    beams.extend(walk_beam_path(contraption, ((pos_x, pos_y - 1), (0, -1))))
                    beams.extend(walk_beam_path(contraption, ((pos_x, pos_y + 1), (0, 1))))

                    break

            case '-':
                if from_direction in (FROM_NORTH, FROM_SOUTH):
                    beams.extend(walk_beam_path(contraption, ((pos_x - 1, pos_y), (-1, 0))))
                    beams.extend(walk_beam_path(contraption, ((pos_x + 1, pos_y), (1, 0))))

                    break

            case '/':
                if from_direction == FROM_NORTH:
                    beams.extend(walk_beam_path(contraption, ((pos_x - 1, pos_y), (-1, 0))))
                elif from_direction == FROM_SOUTH:
                    beams.extend(walk_beam_path(contraption, ((pos_x + 1, pos_y), (1, 0))))
                elif from_direction == FROM_EAST:
                    beams.extend(walk_beam_path(contraption, ((pos_x, pos_y + 1), (0, 1))))
                else: # FROM_WEST
                    beams.extend(walk_beam_path(contraption, ((pos_x, pos_y - 1), (0, -1))))

                break

            case '\\':
                if from_direction == FROM_NORTH:
                    beams.extend(walk_beam_path(contraption, ((pos_x + 1, pos_y), (1, 0))))
                elif from_direction == FROM_SOUTH:
                    beams.extend(walk_beam_path(contraption, ((pos_x - 1, pos_y), (-1, 0))))
                elif from_direction == FROM_EAST:
                    beams.extend(walk_beam_path(contraption, ((pos_x, pos_y - 1), (0, -1))))
                else: # FROM_WEST
                    beams.extend(walk_beam_path(contraption, ((pos_x, pos_y + 1), (0, 1))))
                
                break

        pos_x = pos_x + beam[1][0]
        pos_y = pos_y + beam[1][1]

    return beams

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        contraption: Contraption = [[{"type": c, "energized": 0} for c in l.strip()] for l in f]

    beams: list[Beam] = [((0,0), (1, 0))]

    while len(beams):
        new_beams: list[Beam] = []

        for beam in beams:
            new_beams.extend(walk_beam_path(contraption, beam))

        beams = new_beams

    energized = sum(sum(bool(tile['energized'])for tile in r) for r in contraption)

    print(energized)