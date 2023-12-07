from sys import stdin
from collections import Counter

def type_without_jokers(hand):
    if len(hand) == 1:
        # five of a kind
        return 6
    elif len(hand) == 2:
        if hand.most_common(1)[0][1] == 4:
            # four of a kind
            return 5
        else:
            # full house
            return 4
    elif len(hand) == 3:
        if hand.most_common(1)[0][1] == 3:
            # three of a kind
            return 3
        else:
            # two pairs
            return 2
    elif len(hand) == 4:
        # one pair
        return 1
    else:
        # nothing
        return 0

def type_with_jokers(hand):
    if len(hand) <= 2:
        # only jokers and maybe another number
        # so five of a kind
        return 6
    elif len(hand) == 3:
        if hand.most_common(1)[0][1] == 3 or hand["J"] == 2:
            # can make four of a kind
            return 5
        else:
            # two of one card, two of another card and another single card
            # can make full house
            return 4
    elif len(hand) == 4:
        # two of one card and 3 single cards
        # can make three of a kind
        return 3
    else:
        # five different cards
        # can make a pair
        return 1


def type(hand):
    hand = Counter(hand)

    if "J" not in hand:
        return type_without_jokers(hand)
    else:
        return type_with_jokers(hand)

def order_key(hand):
    card_to_hex = {
        "J": "0", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5",
        "7": "6", "8": "7", "9": "8", "T": "9", "Q": "A", "K": "B",
        "A": "C"
    }

    hand_in_hex = "".join(card_to_hex[card] for card in hand)

    return 0x1000000 * type(hand) + int(hand_in_hex, 16)


hands_bids = []
for line in (l.strip() for l in stdin):
    hand, bid = line.split(" ")
    bid = int(bid)
    hands_bids.append((hand, bid))


hands_bids.sort(key=lambda x: order_key(x[0]))

winnings_sum = 0
for rank, (_, bid) in enumerate(hands_bids, start=1):
    winnings_sum += rank * bid

print(winnings_sum)



