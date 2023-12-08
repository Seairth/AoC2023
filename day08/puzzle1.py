import re

node_pattern = re.compile(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)')

node_map: dict[str, tuple[str, str]] = {}

with open('input.txt', 'r') as f:
    lr = [1 if c == 'R' else 0 for c in f.readline()[:-1]]

    f.readline()

    for line in f:
        match = node_pattern.findall(line)

        node_map[match[0][0]] = (match[0][1], match[0][2])

steps = 0

current_turn = 0
current_node = 'AAA'

while current_node != 'ZZZ':
    steps += 1

    current_node = node_map[current_node][lr[current_turn]]

    current_turn = (current_turn + 1) % len(lr)

print(steps)