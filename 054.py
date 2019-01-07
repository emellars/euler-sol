#Runtime ~0.26s.

import numpy as np

#Allows a list of replacements for str.replace().
def replace_multiple(string, replacements):
    for replacement in replacements:
        string = string.replace(replacement[0], replacement[1])
    return string

#Evaluate highest card in a hand and return a score between 3 and 14.
def high_card(hand):
    hand_values = hand[0]
    return sorted(hand_values)[-1]

#Evaluate highest pair in a hand and return a score between 15 and 27 if it is present.
def one_high_pair(hand):
    hand_values = sorted(hand[:][0])[::-1]
    for card in hand_values:
        hand_values.remove(card)
        if card in hand_values:
            hand_values.remove(card)
            if card in hand_values: return 0
            else: return 13 + card
    return 0

#Evalute lowest pair in a hand and return a score between 15 and 27 if it is present.
def one_low_pair(hand):
    hand_values = sorted(hand[:][0])
    for card in hand_values:
        hand_values.remove(card)
        if card in hand_values:
            hand_values.remove(card)
            if card in hand_values: return 0
            else: return 13 + card
    return 0

#Two pair scores between 31 and 53.
def two_pairs(hand):
    low_pair = one_low_pair(hand)
    high_pair = one_high_pair(hand)
    if low_pair != 0 and high_pair != 0 and low_pair != high_pair: return low_pair + high_pair
    return 0

#Evaluate if four of a kind (score between 244 and 256) is in a hand or, if it is not, three of a kind (score between 54 and 66) and return its score.
def of_a_kind(hand):
    hand_values = sorted(hand[:][0])
    for card in hand_values:
        hand_values.remove(card)
        if card in hand_values:
            hand_values.remove(card)
            if card in hand_values:
                hand_values.remove(card)
                if card in hand_values: return 242 + card
                else: return 52 + card
    return 0

#Straight scores between 67 and 75.
def straight(hand):
    hand_values = sorted(hand[:][0])
    for card in hand_values[:-1]:
        if card + 1 not in hand_values: return 0
    if len(np.unique(hand_values)) == 5: return 65 + hand_values[0]
    else: return 0

#Flush scores 76.
def flush(hand):
    hand_suits = hand[1]
    if len(np.unique(hand_suits)) == 1: return 76
    return 0

#Full house scores between 77 and 243.
def full_house(hand):
    hand_values = sorted(hand[:][0])
    if hand_values[0] == hand_values[1] and hand_values[1] == hand_values[2] and hand_values[-1] == hand_values[-2]: pair = one_high_pair(hand)
    elif hand_values[-1] == hand_values[-2] and hand_values[-2] == hand_values[-3] and hand_values[0] == hand_values[1]: pair = one_low_pair(hand)
    else: return 0
    three_kind = of_a_kind(hand)
    if pair != 0 and three_kind != 0 and three_kind < 67 and len(np.unique(hand_values)) == 2: return pair + 13*three_kind - 641
    return 0

#Straight flush scores between 257 and 265 (265 being a royal flush).
def straight_flush(hand):
    if flush(hand) == 76 and straight(hand) != 0: return 255 + sorted(hand[0][:])[0]
    return 0

#Given a hand, return the highest score.
def score_hand(hand):
    if straight_flush(hand) != 0: return straight_flush(hand)
    elif full_house(hand) != 0: return full_house(hand)
    elif flush(hand) != 0 and flush(hand) > of_a_kind(hand): return flush(hand)
    elif straight(hand) != 0: return straight(hand)
    elif of_a_kind(hand) != 0: return of_a_kind(hand)
    elif two_pairs(hand) != 0: return two_pairs(hand)
    elif one_high_pair(hand) != 0: return one_high_pair(hand)
    else: return high_card(hand)

with open("054.txt", "r") as poker_hands:
    poker_hands = poker_hands.read()

#Substitute faces with their values and assign suits an integer from 1 to 4.
replacements = [["T", "10"], ["J", "11"], ["Q", "12"], ["K", "13"], ["A", "14"], ["C", "1"], ["D", "2"], ["H", "3"], ["S", "4"]]
poker_hands = [replace_multiple(elem, replacements) for elem in poker_hands.split()]

#Convert poker data to a form where each element is a list containing a particular hand for both players, i.e. poker_hands[hand, player, card, value=0/suit=1].
poker_hands = [[int(elem[0:-1]), int(elem[-1])] for elem in poker_hands]
poker_hands = np.reshape(poker_hands, (1000, 2, 5, 2))
#Convert poker data to the form poker_hands[hand, player, values=0/suits=1, card]
poker_hands = np.array([[np.transpose(elem[0]), np.transpose(elem[1])] for elem in poker_hands])

player_scores = []
#Assigns the maximum score to each hand.
for hands in poker_hands:
    player_scores.append([score_hand(hands[0]), score_hand(hands[1])])

#For ties, determine the winner by the highest card.
for i in range(len(player_scores)):
    if player_scores[i][0] == player_scores[i][1]:
        player_scores[i][0] = high_card(poker_hands[i][0])
        player_scores[i][1] = high_card(poker_hands[i][1])

player1_wins = 0
for scores in player_scores:
    if scores[0] > scores[1]: player1_wins += 1

print(player1_wins)
