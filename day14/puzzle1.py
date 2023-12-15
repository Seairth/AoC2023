
def tilt_north(platform: list[list[str]]) -> list[list[str]]:
    for step in range(len(platform) - 1, 0, -1):
        for row_idx in range(step):
            row1 = platform[row_idx]
            row2 = platform[row_idx + 1]

            for col_idx, col in enumerate(row1):
                if col == '.' and row2[col_idx] == 'O':
                    row1[col_idx] = 'O'
                    row2[col_idx] = '.'

    return platform

load = 0

with open('input.txt', 'r') as f:
    platform = [list(l.strip()) for l in f]

    platform = tilt_north(platform)

    max_load = len(platform)

    for idx, row in enumerate(platform):
        load += (row.count('O') * (max_load - idx))

print(load)