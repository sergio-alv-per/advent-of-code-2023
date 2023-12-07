from sys import stdin
from collections import Counter


def type(hand):
    hand = Counter(hand)

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

def order_key(hand):
    card_to_hex = {
        "2": "0", "3": "1", "4": "2", "5": "3", "6": "4", "7": "5",
        "8": "6", "9": "7", "T": "8", "J": "9", "Q": "A", "K": "B",
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



