
from typing import Iterator, Sequence


def is_match(data: str, start: int, damaged_groups: Sequence[int]) -> Iterator[bool]:

    if (sum(damaged_groups) + len(damaged_groups) - 1) > (len(data) - start):
        yield False
    else:
        if data[start] != '#':
            # either `.` (operational) or '?' (could be operational)
            yield from is_match(data, start + 1, damaged_groups)

        if data[start] != '.':
            # either '#' (damaged) or '?' (could be damaged)
            stop = start + damaged_groups[0]

            if '.' in data[(start + 1):stop]:
                yield False
            else:
                if len(damaged_groups) > 1:
                    if data[stop] != '#' and len(data) > (stop + 1):
                        yield from is_match(data, stop + 1, damaged_groups[1:])
                    else:
                        yield False
                else:
                    if len(data) > stop:
                        yield (not '#' in data[stop:])
                    else:
                        yield True


def read_record(record: str) -> tuple[str, list[int]]:
    parts = record.strip().split(' ')
    damaged_counts = [int(n) for n in parts[1].split(',')]

    return (parts[0], damaged_counts)


matches = 0

with open('input.txt', 'r') as f:
    for record in f:
        field, damaged_groups = read_record(record)
        matches += sum(is_match(field, 0, damaged_groups))

print(matches)