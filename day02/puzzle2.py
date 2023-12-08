from functools import reduce
import re

sum_power = 0

game_pattern = re.compile(r'Game (\d+): (.+)')
round_pattern = re.compile(r'(\d+) (red|green|blue)')

with open('input.txt', 'r') as f:
    for line in f:
        max_cubes = { 'red': 0, 'green': 0, 'blue': 0 }

        game_info = game_pattern.findall(line)

        game_results = game_info[0][1]

        for round in game_results.split(';'):
            round_info = round_pattern.findall(round)

            for cubes in round_info:
                max_cubes[cubes[1]] = max(max_cubes[cubes[1]], int(cubes[0]))

        sum_power += reduce(lambda x, y: x * y, max_cubes.values())

print(sum_power)