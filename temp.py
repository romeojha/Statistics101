import itertools
import random
from collections import Counter


# x=[[('2', 'heart'), ('2', 'spades'), ('2', 'spades')],
# [('8', 'spades'), ('7', 'spades'), ('6', 'spades')],
# [('13', 'diamond'), ('1', 'clubs'), ('10', 'clubs')],
# [('13', 'spades'), ('12', 'clubs'), ('11', 'spades')],
# [('1', 'heart'), ('7', 'diamond'), ('4', 'heart')],
# [('12', 'diamond'), ('8', 'clubs'), ('12', 'clubs')],
# [('2', 'spades'), ('11', 'heart'), ('4', 'diamond')],
# [('6', 'spades'), ('4', 'diamond'), ('3', 'clubs')],
# [('4', 'diamond'), ('11', 'spades'), ('5', 'diamond')],
# [('6', 'heart'), ('3', 'heart'), ('13', 'heart')]]

def is_triple(cards):
    # Sort the cards by their values
    cards.sort(key=lambda card: card[0])

    # Check if the values are consecutive
    for i in range(2):
        if float(cards[i][0]) != float(cards[i + 1][0]):
            return 0.0
    return 6.0

def isrun_double(cards):
    # Sort the cards by their values
    cards.sort(key=lambda card: card[0])

    # Check if the values are consecutive
    for i in range(2):
        if float(cards[i][0]) != float(cards[i + 1][0]) - 1:
            if (cards[i][1] != cards[i + 1][1]):
                return 0.0
    return 5.0

def is_run(cards):
    # Sort the cards by their values
    cards.sort(key=lambda card: float(card[0]))
    # Check if the values are consecutive
    for i in range(2):
        if float(cards[i][0]) != float(cards[i + 1][0]) - 1:
            return 0.0
    return 4.0

def is_suit(cards):
    sum=0
    # Check if the cards list has at least 3 cards
    if len(cards) < 3:
        return 0.0
    for i in range(2):
        # Check if the suit is a non-empty string
        if not isinstance(cards[i][1], str) or len(cards[i][1]) == 0:
            return 0
        # Check if the suits are different
        if cards[i][1] != cards[i + 1][1]:
            return 0.0
        sum+=int(cards[i][0])
    if sum >= 4:
        return 3.1
    if sum >= 8:
        return 3.2
    if sum >= 12:
        return 3.3
    if sum >= 16:
        return 3.4
    if sum >= 20:
        return 3.5
    if sum >= 24:
        return 3.6
    if sum >= 28:
        return 3.7
    if sum >= 32:
        return 3.8
    if sum >= 36:
        return 3.9
    return 3.0

def improvement(x,i):
    return x[0]

def has_two_cards_same_value_diff_colors(cards):
    # cards= improvement(cards)
    card_values = [int(card[0]) for card in cards] #imporeveceemnt
    print(card_values)
    if 2 in card_values and card_values.count(2) == 2:
        return 2.2 
    if 3 in card_values and card_values.count(3) == 2:
        return 2.21 
    if 4 in card_values and card_values.count(4) == 2:
        return 2.22 
    if 5 in card_values and card_values.count(5) == 2:
        return 2.25 
    if 6 in card_values and card_values.count(6) == 2:
        return 2.3 
    if 7 in card_values and card_values.count(7) == 2:
        return 2.4 
    if 8 in card_values and card_values.count(8) == 2:
        return 2.5
    if 9 in card_values and card_values.count(9) == 2:
        return 2.6
    if 10 in card_values and card_values.count(10) == 2:
        return 2.7 
    if 11 in card_values and card_values.count(11) == 2:
        return 2.8 
    if 12 in card_values and card_values.count(12) == 2:
        return 2.9
    if 1 in card_values and card_values.count(1) == 2:
        return 2.99
    else:
        return 0.0  


def has_highest(cards):
    sum=[]
    card_values = [int(card[0]) for card in cards]    
    for i in range(2):
        sum+=int(cards[i][0])
    if sum >= 4:
        return 1.1
    if sum >= 8:
        return 1.2
    if sum >= 12:
        return 1.3
    if sum >= 16:
        return 1.4
    if sum >= 20:
        return 1.5
    if sum >= 24:
        return 1.6
    if sum >= 28:
        return 1.7
    if sum >= 32:
        return 1.8
    if sum >= 36:
        return 1.9
    print(1.0)

# print(is_triple(x[0]))
# print((x[0]))
# print(x[0].sort(key=lambda x: x[0][0]))
func = [has_two_cards_same_value_diff_colors, is_suit, is_run, is_triple,has_highest ]

# print(is_triple(x[0]))


def check_all(x, func): # x should be single point
    highest_point = 0
    for f in func:
        result = f(x)
        if result > highest_point:
            highest_point = result
        return float(highest_point)


def create_x():
    colors = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    deck = list(itertools.product(values, colors))
    return deck

def deal_hands(deck, num_hands, cards_per_hand):
    if num_hands * cards_per_hand > len(deck):
        return "Not enough cards in the deck to deal the requested number of hands and cards per hand."

    random.shuffle(deck)
    hands = [[deck[i:i+cards_per_hand] for i in range(0, num_hands * cards_per_hand, cards_per_hand)]]
    return hands






# for i in range(10000):
#     o=create_x()
#     for i in range(10):
#         a.append(check_all(o[i], func))
#     p.append(a.index(max(a)))
# print(p)
a=[]
p=[]

# Create the deck
deck = create_x()

# Deal three cards for ten hands
num_hands = 10
cards_per_hand = 3
hands = deal_hands(deck, num_hands, cards_per_hand)

formatted_hands = [list(hand) for hand in hands]
print(check_all(formatted_hands[0][0],func))


for i in range(10):
    # print(formatted_hands[0][i])
    a.append(check_all(formatted_hands[0][i], func))


print(a)




#temp
# def has_two(cards):
#     card_values=[int(card[0]) for card in cards]
#     print(card_values)
#     if card_values.count(12) == 2:
#         return 2.9 

# # Example usage
# hand = [('12', 'hearts'), ('12', 'spades'), ('4', 'clubs')]

# results = has_two(hand)
# print(results)
# print(results)