import re

card_pattern = re.compile(r"Card\s+\d+:(.+)\|(.+)")

with open('input.txt', 'r') as f:
    cards = f.readlines()

card_count = [1] * len(cards)

for idx, card in enumerate(cards):
    wins = 0

    match = card_pattern.findall(card)

    winning_numbers = [int(n) for n in match[0][0].split(' ') if len(n)]
    my_numbers = [int(n) for n in match[0][1].split(' ') if len(n)]

    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            wins += 1

    if wins > 0:
        for idx2 in range(idx + 1, idx + wins + 1):
            card_count[idx2] += card_count[idx]

sum_cards = sum(card_count)

print(sum_cards)