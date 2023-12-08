import re

numbers_pattern = re.compile(r"(\d+)")

with open('input.txt', 'r') as f:
    race_records = f.readlines()

times = tuple(map(int, numbers_pattern.findall(race_records[0].replace(' ', ''))))
distances = tuple(map(int, numbers_pattern.findall(race_records[1].replace(' ', ''))))


calc_distance = lambda t, s: (s * (t - s))

margin = 1

for race, time in enumerate(times):
    distance = distances[race]

    min_delay = 0

    while calc_distance(time, min_delay) < distance:
        min_delay += 1

    # max_delay = min_delay

    # while calc_distance(time, max_delay) > distance:
        #max_delay += 1

    max_delay = time - min_delay + 1

    # no need to subtract one because we're treating it as [min, max)

    margin *= (max_delay - min_delay)

print(margin)