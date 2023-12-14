from typing import Iterator

def generate_maps(iter: Iterator[str]) -> Iterator[list[str]]:
    map: list[str] = []

    for row in iter:
        row = row.strip()

        if len(row):
            map.append(row)
        else:
            yield map
            map = []

    yield map

def is_symmetric(map: list[str], start_row: int) -> bool:
    for offset in range(start_row + 1):
        top_idx = start_row - offset
        bottom_idx = start_row + offset + 1

        if map[top_idx] != map[bottom_idx]:
            break

        if top_idx == 0 or bottom_idx == (len(map) - 1):
            return True
        
    return False

def find_horizontal_mirror(map: list[str], ignore = -1) -> int | None:
    for idx in range(len(map) - 1):
        if is_symmetric(map, idx) and idx != ignore:
            return idx
        
    return None

def transpose_map(map: list[str]) -> list[str]:
    new_map: list[str] = []

    for idx in range(len(map[0])):
        new_row = ""

        for row in map:
            new_row += row[idx]

        new_map.append(new_row)

    return new_map

def find_vertical_mirror(map: list[str]) -> int | None:
    return find_horizontal_mirror(transpose_map(map))

def generate_clean_map_candidates(map:list[str]) -> Iterator[list[str]]:
    for row_idx, row in enumerate(map):
        candidate_map: list[str] = []
        
        if row_idx > 0:
            candidate_map.extend(map[0:row_idx])

        candidate_map.append('')

        if row_idx < len(map) - 1:
            candidate_map.extend(map[(row_idx + 1):])

        for col_idx, col in enumerate(row):
            new_row = list(row)
            new_row[col_idx] = '.' if col == '#' else '#'
            candidate_map[row_idx] = str.join('', new_row)

            yield candidate_map

def find_smudged_horizontal_mirror(map: list[str], ignore = -1) -> int | None:
    for clean_map in generate_clean_map_candidates(map):
        mirror = find_horizontal_mirror(clean_map, ignore)

        if mirror is not None:
            return mirror
    
    return None

def find_smudged_vertical_mirror(map: list[str], ignore = -1) -> int | None:
    return find_smudged_horizontal_mirror(transpose_map(map), ignore)
    
mirror_sums = 0

with open('input.txt', 'r') as f:
    for map in generate_maps(f):

        mirror = find_horizontal_mirror(map)

        if mirror is not None:
            new_mirror = find_smudged_horizontal_mirror(map, mirror)

            if new_mirror is not None:
                mirror_sums += 100 * (new_mirror + 1)
            else:
                new_mirror = find_smudged_vertical_mirror(map)
                assert(new_mirror is not None)

                mirror_sums += (new_mirror + 1)
        else:
            mirror = find_vertical_mirror(map)
            assert (mirror is not None)

            new_mirror = find_smudged_vertical_mirror(map, mirror)

            if new_mirror is not None:
                mirror_sums += (new_mirror + 1)
            else:
                try:
                    new_mirror = find_smudged_horizontal_mirror(map)
                    assert(new_mirror is not None)
                    mirror_sums += 100 * (new_mirror + 1)
                except:
                    print("vert:", mirror)
                    for row in map:
                        print(row)
                    exit()

print(mirror_sums)