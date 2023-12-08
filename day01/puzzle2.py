import re
from typing import Final

number_map: Final = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}     

sum_cal = 0

# This uses a capture group to find _overlapping_ matches

pattern = re.compile('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))')

with open('input.txt', 'r') as f:
    for line in f:
        numbers = [match.group(1) for match in pattern.finditer(line)]

        first = number_map.get(numbers[0], numbers[0])
        last = number_map.get(numbers[-1], numbers[-1])

        sum_cal += int(first + last)

print(sum_cal)