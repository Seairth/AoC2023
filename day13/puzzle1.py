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

def find_horizontal_mirror(map: list[str]) -> int | None:
    for idx in range(len(map) - 1):
        if is_symmetric(map, idx):
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

    
mirror_sums = 0

with open('input.txt', 'r') as f:
    for map in generate_maps(f):
        mirror = find_horizontal_mirror(map)

        if mirror is not None:
            mirror_sums += 100 * (mirror + 1)
        else:
            mirror = find_vertical_mirror(map)
            
            assert(mirror is not None)
            mirror_sums += (mirror + 1)

print(mirror_sums)