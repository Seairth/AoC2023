def expand_universe(map:list[str]) -> list[list[str]]:
    expanded_map: list[list[str]] = []

    for row in map:
        if not '#' in row:
            expanded_map.append([c for c in row])

        expanded_map.append([c for c in row])

    new_col_idx = 0

    for orig_col_idx in range(len(map[0])):
        for row in map:
            if row[orig_col_idx] == '#':
                break
        else:
            # empty column
            new_col_idx += 1
            for row in expanded_map:
                row.insert(new_col_idx, '.')

        new_col_idx += 1

    return expanded_map

with open('input.txt', 'r') as f:
    map = [l.strip() for l in f]

map = expand_universe(map)

galaxies: list[tuple[int, int]] = []

for row_idx, row in enumerate(map):
    for col_idx, col in enumerate(row):
        if col == '#':
            galaxies.append((row_idx, col_idx))

sum_min_distances = 0

for idx1, pos1 in enumerate(galaxies[:-1]):
    for idx2, pos2 in enumerate(galaxies[(idx1 + 1):]):
        sum_min_distances += abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

print(sum_min_distances)