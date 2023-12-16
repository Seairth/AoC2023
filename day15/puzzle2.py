
from functools import reduce

Box = list[tuple[str, int]]

def calculate_hash(value: str) -> int:
    return reduce(lambda h, c: (((h + ord(c)) * 17) % 256), value, 0)

def process_instruction(instruction: str, boxes: list[Box]):
    if '-' in instruction:
        # remove
        label = instruction[:-1]
        labeled_lens = (label, 0)

    else:
        # add/replace
        label, strength = instruction.split('=')
        labeled_lens = (label, int(strength))

    box = boxes[calculate_hash(labeled_lens[0])]

    try:
        slot = next(i for i, v in enumerate(box) if v[0] == labeled_lens[0])

        if labeled_lens[1] > 0:
            box[slot] = labeled_lens
        else:
            box.pop(slot)

    except StopIteration:
        if labeled_lens[1] > 0:
            box.append(labeled_lens)

def calculate_strength(boxes: list[Box]) -> int:
    strength = 0

    for box_idx, box in enumerate(boxes):
        for slot_idx, slot in enumerate(box):
            strength += (box_idx + 1) * (slot_idx + 1) * slot[1]

    return strength

with open('input.txt', 'r') as f:
    startup_sequence = f.readline()

# there are 256 boxes, each of which contains an ordered sequence of (label, focal length) pairs
# NOTE: `boxes = [[]] * 256` does not work, because all 256 lists will be the _same object_!
boxes: list[Box] = [[] for _ in range(256)]

start = 0

for idx, c in enumerate(startup_sequence):
    if c == ',':
        process_instruction(startup_sequence[start:idx], boxes)
        start = idx + 1

process_instruction(startup_sequence[start:], boxes)

print(calculate_strength(boxes))
