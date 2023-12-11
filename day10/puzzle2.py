def find_start(map: list[str]) -> tuple[int, int]:

    for idx, row in enumerate(map):
        if "S" in row:
            return (idx, row.index("S"))

    return (-1, -1) # should never execute.  Just making pylance happy.

def at_start(map: list[str], pos: tuple[int, int]) -> bool:
    return map[next_pipe[0]][next_pipe[1]] == "S"


def can_travel_north(map: list[str], pos: tuple[int, int]) -> bool:
    not_at_edge = (pos[0] > 0)
    return not_at_edge and map[pos[0] - 1][pos[1]] in "|7FS"

def can_travel_south(map: list[str], pos: tuple[int, int]) -> bool:
    not_at_edge = (pos[0] < len(map) - 1)
    return not_at_edge and map[pos[0] + 1][pos[1]] in "|JLS"

def can_travel_east(map: list[str], pos: tuple[int, int]) -> bool:
    not_at_edge = (pos[1] < len(map[pos[0]]) - 1)
    return not_at_edge and map[pos[0]][pos[1] + 1] in "-7JS"

def can_travel_west(map: list[str], pos: tuple[int, int]) -> bool:
    not_at_edge = (pos[1] > 0)
    return not_at_edge and map[pos[0]][pos[1] - 1] in "-FLS"

with open('input.txt', 'r') as f:
    map = f.readlines()

start = find_start(map)

# NOTE:  This does not work for a general solution.  In my data set, I
# visually noted that two of the possible starting paths were not possible,
# so I could trivially start with one of the two valid paths. A more robust
# solution would programmatically check for this condition.

path = [start]

for next_pipe in [(start[0], start[1] - 1, 'E')]:
    while not at_start(map, next_pipe[:2]):
        path.append(next_pipe[:2])

        symbol = map[next_pipe[0]][next_pipe[1]]

        match next_pipe[2]:
            case 'N':
                match symbol:
                    case '|' if can_travel_south(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0] + 1, next_pipe[1], 'N')
                        continue

                    case 'L' if can_travel_east(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0], next_pipe[1] + 1, 'W')
                        continue

                    case 'J' if can_travel_west(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0], next_pipe[1] - 1, 'E')
                        continue

            case 'S':
                match symbol:
                    case '|' if can_travel_north(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0] - 1, next_pipe[1], 'S')
                        continue

                    case 'F' if can_travel_east(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0], next_pipe[1] + 1, 'W')
                        continue

                    case '7' if can_travel_west(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0], next_pipe[1] - 1, 'E')
                        continue

            case 'E':
                match symbol:
                    case '-' if can_travel_west(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0], next_pipe[1] - 1, 'E')
                        continue

                    case 'L' if can_travel_north(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0] - 1, next_pipe[1], 'S')
                        continue

                    case 'F' if can_travel_south(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0] + 1, next_pipe[1], 'N')
                        continue

            case 'W':
                match symbol:
                    case '-' if can_travel_east(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0], next_pipe[1] + 1, 'W')
                        continue

                    case 'J' if can_travel_north(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0] - 1, next_pipe[1], 'S')
                        continue

                    case '7' if can_travel_south(map, next_pipe[:2]):
                        next_pipe = (next_pipe[0] + 1, next_pipe[1], 'N')
                        continue
        
        # if we get here, we encountered a dead end
        break
    else:
        # if we get here, we have found the loop!
        break

num_inside = 0

# scan each row, toggling the "inside" flag when encountering a |, a pair of FJ, or a pair of L7
for row_idx, row in enumerate(map):
    inside = False
    last_corner = '-'

    for col_idx, _ in enumerate(row):

        if (row_idx, col_idx) in path:
            symbol = map[row_idx][col_idx]

            if symbol == '|':
                inside = not inside

            elif symbol in "7FJL":
                # At a corner
                if last_corner in 'FL':
                    if last_corner == 'F' and symbol == 'J':
                        inside = not inside
                    elif last_corner == 'L' and symbol == '7':
                        inside = not inside
                    
                last_corner = symbol

            continue

        if inside:
            num_inside += 1

print(num_inside)