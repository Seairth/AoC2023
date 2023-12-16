
from functools import reduce

def hash(value: str) -> int:
    return reduce(lambda h, c: (((h + ord(c)) * 17) % 256), value, 0)

hash_sum = 0

with open('input.txt', 'r') as f:
    startup_sequence = f.readline()


start = 0

for idx, c in enumerate(startup_sequence):
    if c == ',':
        hash_sum += hash(startup_sequence[start:idx])
        start = idx + 1

hash_sum += hash(startup_sequence[start:])

print(hash_sum)