def read_map(almanac: list[str], line: int) -> tuple[dict[range, range], int]:
    map: dict[range, range] = {}

    while(line < len(almanac) and len(almanac[line].strip())):
        values = [int(v) for v in almanac[line].split(' ')]
        src = range(values[1], values[1] + values[2])
        dst = range(values[0], values[0] + values[2])

        map[src] = dst

        line += 1

    return map, line

def get_mapped_value(map: dict[range, range], src: int) -> int:
    for k, v in map.items():
        if src in k:
            return v[k.index(src)]
    
    return src

with open('input.txt', 'r') as f:
    almanac = f.readlines()

line = 0

seeds = [int(v) for v in almanac[line].split(' ')[1:]]

seed_to_soil, line = read_map(almanac, line + 3)
soil_to_fertilizer, line = read_map(almanac, line + 2)
fertilizer_to_water, line = read_map(almanac, line + 2)
water_to_light, line = read_map(almanac, line + 2)
light_to_temperature, line = read_map(almanac, line + 2)
temperature_to_humidity, line = read_map(almanac, line + 2)
humidity_to_location, _ = read_map(almanac, line + 2)

locations: list[int] = []

for seed in seeds:
    # this sequence seems ideal for partials and function composition
    soil = get_mapped_value(seed_to_soil, seed)
    fertilizer = get_mapped_value(soil_to_fertilizer, soil)
    water = get_mapped_value(fertilizer_to_water, fertilizer)
    light = get_mapped_value(water_to_light, water)
    temperature = get_mapped_value(light_to_temperature, light)
    humidity = get_mapped_value(temperature_to_humidity, temperature)
    location = get_mapped_value(humidity_to_location, humidity)

    locations.append(location)

print(min(locations))
