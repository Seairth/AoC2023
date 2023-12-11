def calc_expansion(map:list[str], factor = 1) -> tuple[list[int], list[int]]:
    row_expansion: list[int] = []
    col_expansion: list[int] = []

    for row in map:
        col_expansion.append(1 if '#' in row else factor)

    for orig_col_idx in range(len(map[0])):
        for row in map:
            if row[orig_col_idx] == '#':
                row_expansion.append(1)
                break
        else:
            # empty column
            row_expansion.append(factor)

    return row_expansion, col_expansion

def get_galaxy_coords(map: list[str]) -> list[tuple[int, int]]:
    coords: list[tuple[int, int]] = []

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col == '#':
                coords.append((row_idx, col_idx))
    
    return coords

with open('input.txt', 'r') as f:
    map = [l.strip() for l in f]

row_expansion, col_expansion = calc_expansion(map, 1_000_000)
coords = get_galaxy_coords(map)

sum_min_distances = 0

for idx1, pos1 in enumerate(coords[:-1]):
    for idx2, pos2 in enumerate(coords[(idx1 + 1):]):

        row_min, row_max = sorted((pos1[0], pos2[0]))
        col_min, col_max = sorted((pos1[1], pos2[1]))

        sum_min_distances += sum(row_expansion[col_min:col_max]) + sum(col_expansion[row_min:row_max])

print(sum_min_distances)