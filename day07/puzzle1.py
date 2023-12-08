import re
from typing import Final

FIVE_OF_A_KIND: Final = 6
FOUR_OF_A_KIND: Final = 5
FULL_HOUSE: Final = 4
THREE_OF_A_KIND: Final = 3
TWO_PAIR: Final = 2
ONE_PAIR: Final = 1
HIGH_CARD: Final = 0

def card_strength(card: str) -> int:
    return "23456789TJQKA".index(card)

def hand_strength(hand: str) -> int:
    sorted_hand = sorted(hand)

    match sorted_hand.count(sorted_hand[2]):
        case 5:
            return FIVE_OF_A_KIND

        case 4:
            return FOUR_OF_A_KIND
    
        case 3:
            if sorted_hand.count(sorted_hand[1]) == 2 or sorted_hand.count(sorted_hand[3]) == 2:
                return FULL_HOUSE

            return THREE_OF_A_KIND
            
        case 2:
            if sorted_hand.count(sorted_hand[0]) == 2 or sorted_hand.count(sorted_hand[4]) == 2:
                return TWO_PAIR
            
            return ONE_PAIR
    
    # middle card is a single.  Check for pairs on either side.

    if sorted_hand.count(sorted_hand[1]) == 2 or sorted_hand.count(sorted_hand[3]) == 2:
        if sorted_hand.count(sorted_hand[1]) == 2 and sorted_hand.count(sorted_hand[3]) == 2:
            return TWO_PAIR
    
        return ONE_PAIR

    return HIGH_CARD

class Hand:
    cards: str
    bid: int

    def __init__(self, cards:str, bid:int) -> None:
        self.cards = cards
        self.bid = bid
        self.strength = hand_strength(cards)
    
    def __lt__(self, other: "Hand") -> bool:
        # This magic method is required for sorting objects of this type

        if self.strength == other.strength:
            for idx, card in enumerate(self.cards):
                strength = card_strength(card)
                other_strength = card_strength(other.cards[idx])

                if strength == other_strength:
                    continue

                return strength < other_strength

        return self.strength < other.strength

hand_pattern = re.compile(r"([23456789TJQKA]{5})\s+(\d+)")

hands: list[Hand] = []

with open('input.txt', 'r') as f:
    for line in f:
        match = hand_pattern.findall(line)
        hands.append(Hand(match[0][0], int(match[0][1])))

hands.sort()

winnings = 0

for idx, hand in enumerate(hands):
    winnings += (idx + 1) * hand.bid

print(winnings)