from typing import Sequence


is_digit = lambda c: c in '0123456789'
is_symbol = lambda c: c == '*'

def find_next_gears(map: list[str], row: int, col: int) -> tuple[int, int, Sequence[tuple[int, int]]]:
    '''
    Starting at [row, col], find the next gear in the row. Return values are:
    * Gear found: col immediately after the number, the gear number, and the [row, col] of the gear
    * Number found: col immediately after the number, zero for the gear number, None for the [row, col]
    * End of row: length of the row, zero for the part number, None for the [row, col]
    '''

    part_number = 0
    gear_centers = []

    curr_row = map[row]

    while col < len(curr_row):
        if is_digit(curr_row[col]):
            break

        col += 1
    else:
        return col, part_number, gear_centers


    part_str = ""

    while col < len(curr_row) and is_digit(curr_row[col]):
        part_str += curr_row[col]

        if row > 0:
            above_row = map[row - 1]
            if (col > 0 and is_symbol(above_row[col - 1])): gear_centers.append((row - 1, col - 1))
            if is_symbol(above_row[col]): gear_centers.append((row - 1, col))
            if (col < (len(above_row) - 1) and is_symbol(above_row[col + 1])): gear_centers.append((row - 1, col + 1))

        if (col > 0 and is_symbol(curr_row[col - 1])): gear_centers.append((row, col - 1))
        if (col < (len(curr_row) - 1) and is_symbol(curr_row[col + 1])): gear_centers.append((row, col + 1))

        if row < len(map) - 1:
            below_row = map[row + 1]
            if (col > 0 and is_symbol(below_row[col - 1])): gear_centers.append((row + 1, col - 1))
            if is_symbol(below_row[col]): gear_centers.append((row + 1, col))
            if (col < (len(below_row) - 1) and is_symbol(below_row[col + 1])): gear_centers.append((row + 1, col + 1))

        col += 1
    else:
        if len(gear_centers):
            gear_centers = list(set(gear_centers))
            part_number = int(part_str)

    return col, part_number, gear_centers

sum_gear_ratios = 0

gears: dict[tuple[int, int], list[int]] = {}

with open('input.txt', 'r') as f:
    map = [line[:-1] for line in f]

for row in range(len(map)):
    col = 0

    while col < len(map[row]):
        col, part, centers = find_next_gears(map, row, col)

        for pos in centers:
            gear_set = gears.get(pos, [])
            gear_set.append(part)
            gears[pos] = gear_set

for gear_set in gears.values():
    if len(gear_set) == 2:
        sum_gear_ratios += (gear_set[0] * gear_set[1])

print(sum_gear_ratios)