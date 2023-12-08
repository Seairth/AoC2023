import re

card_pattern = re.compile(r"Card\s+\d+:(.+)\|(.+)")

sum_points = 0

with open('input.txt', 'r') as f:
    for card in f:
        card_points = 0

        match = card_pattern.findall(card)

        winning_numbers = [int(n) for n in match[0][0].split(' ') if len(n)]
        my_numbers = [int(n) for n in match[0][1].split(' ') if len(n)]

        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                card_points = 1 if card_points == 0 else card_points * 2

        sum_points += card_points

print(sum_points)