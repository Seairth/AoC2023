from typing import Iterator
from puzzle1 import walk_beam_path, Contraption, Beam

def generate_start_beams(contraption: Contraption) -> Iterator[Beam]:
    num_rows = len(contraption)
    num_cols = len(contraption[0])

    for idx in range(num_rows):
        yield ((0, idx), (1, 0))
        yield ((num_cols - 1, idx), (-1, 0))

    for idx in range(num_cols):
        yield ((idx, 0), (0, 1))
        yield ((idx, num_rows - 1), (0, -1))

def reset_energized(contraption: Contraption):
    for row in contraption:
        for tile in row:
            tile['energized'] = 0

with open('input.txt', 'r') as f:
    contraption: Contraption = [[{"type": c, "energized": 0} for c in l.strip()] for l in f]

max_energized = 0

for start_beam in generate_start_beams(contraption):
    beams: list[Beam] = [start_beam]

    while len(beams):
        new_beams: list[Beam] = []

        for beam in beams:
            new_beams.extend(walk_beam_path(contraption, beam))

        beams = new_beams

    energized = sum(sum(bool(tile['energized'])for tile in r) for r in contraption)

    max_energized = max(max_energized, energized)

    # NOTE: the following function is an example of why data should be immutable
    # whenever possible. Each iteration of the for-loop requires the energized value
    # initially be zero for all tiles.  It took me a while to realize I wasn't resetting
    # energized at the end of each loop.  If, instead, the contraption was treated as
    # immutable, then the energized state would have been separate and could have been
    # initialized each time at the top of the loop, preventing this subtle bug.  While
    # this could be seen as just another form of a reset, the point is that it (probably)
    # would have been a more obvious bug if a dedicated energized state object had been
    # initialized only once outside of the loop.

    reset_energized(contraption)

print(max_energized)