import re

sum_valid_games = 0

game_pattern = re.compile(r'Game (\d+): (.+)')
round_pattern = re.compile(r'(\d+) (red|green|blue)')

max_vals = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt', 'r') as f:
    for line in f:
        game_info = game_pattern.findall(line)

        game_id = game_info[0][0]
        game_results = game_info[0][1]

        for round in game_results.split(';'):
            round_info = round_pattern.findall(round)

            for cubes in round_info:
                if int(cubes[0]) > max_vals[cubes[1]]:
                    break
            else:
                continue

            break
        else:
            sum_valid_games += int(game_id)

print(sum_valid_games)