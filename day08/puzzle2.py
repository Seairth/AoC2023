import math
import re

node_pattern = re.compile(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)')

node_map: dict[str, tuple[str, str]] = {}

with open('input.txt', 'r') as f:
    lr = [1 if c == 'R' else 0 for c in f.readline()[:-1]]

    f.readline()

    for line in f:
        match = node_pattern.findall(line)

        node_map[match[0][0]] = (match[0][1], match[0][2])

# NOTE: This technique only works because the data is organized such that
# you only have to find the first encounter of `xxZ` for each starting point,
# which is not obvious from the problem description! The final answer is then
# the LCM of the lengths of the paths to the first `xxZ`.

path_lengths: list[int] = []

for node in [node for node in node_map.keys() if node[2] == 'A']:
    steps = 0
    current_turn = 0
    
    while node[2] != 'Z':
        steps += 1

        node = node_map[node][lr[current_turn]]

        current_turn = (current_turn + 1) % len(lr)

    path_lengths.append(steps)

print(math.lcm(*path_lengths))