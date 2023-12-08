is_digit = lambda c: c in '0123456789'
is_space = lambda c: c == '.'
is_symbol = lambda c: not (is_digit(c) or is_space(c))

def find_next_part(map: list[str], row: int, col: int) -> tuple[int, int]:
    '''
    Starting at [row, col], find the next part in the row. Return values are:
    * Part found: col immediately after the number and the part number.
    * Number found: col immediately after the number and zero for the part number.
    * End of row: length of the row and zero for the part number.
    '''

    part_number = 0

    curr_row = map[row]

    while col < len(curr_row):
        if is_digit(curr_row[col]):
            break

        col += 1
    else:
        return col, part_number


    is_part = False
    part_str = ""

    while col < len(curr_row) and is_digit(curr_row[col]):
        part_str += curr_row[col]

        if row > 0:
            above_row = map[row - 1]
            is_part = is_part or (col > 0 and is_symbol(above_row[col - 1]))
            is_part = is_part or is_symbol(above_row[col])
            is_part = is_part or (col < (len(above_row) - 1) and is_symbol(above_row[col + 1]))

        is_part = is_part or (col > 0 and is_symbol(curr_row[col - 1]))
        is_part = is_part or (col < (len(curr_row) - 1) and is_symbol(curr_row[col + 1]))

        if row < len(map) - 1:
            below_row = map[row + 1]
            is_part = is_part or (col > 0 and is_symbol(below_row[col - 1]))
            is_part = is_part or is_symbol(below_row[col])
            is_part = is_part or (col < (len(below_row) - 1) and is_symbol(below_row[col + 1]))

        col += 1
    else:
        if is_part:
            part_number = int(part_str)

    return col, part_number

sum_parts = 0

with open('input.txt', 'r') as f:
    map = [line[:-1] for line in f]

    for row in range(len(map)):
        col = 0

        while col < len(map[row]):
            col, part = find_next_part(map, row, col)

            sum_parts += part

print(sum_parts)