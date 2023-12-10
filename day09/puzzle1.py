import numpy as np
from functools import reduce


sum_next_seq = 0

with open('input.txt', 'r') as f:
    for line in f:
        seq = [int(n) for n in line.split(' ')]

        seqs = [seq]

        while reduce(lambda t, s: t or s != 0, seqs[-1], False):
            seqs.append(np.diff(seqs[-1]).tolist())

        seqs.pop()
        last_val = 0

        while len(seqs):
            seq = seqs.pop()
            last_val = seq[-1] + last_val

        sum_next_seq += last_val

print(sum_next_seq)