import sys
import math
import numpy as np
import itertools
import random

digits = list(range(10))
number_length = int(input())
correct_digits = [None] * number_length
position_possible = np.ones(shape=(number_length, len(digits)), dtype=bool)

# Can't place "0" on first position
position_possible[0, 0] = False

def random_possible_number(correct_digits, position_possible):
    guess_digits = []
    for position, digit in enumerate(correct_digits):
        if digit is None:
            possible_digits = np.nonzero(position_possible[position, :])[0]
            possible_digits = [d for d in possible_digits if d not in guess_digits]
            print(position, possible_digits, file=sys.stderr)
            digit = random.choice(possible_digits)
        guess_digits.append(digit)
    return guess_digits

def update_possible(correct_digits, position_possible, bulls, cows, guess_digits):
    # update possibilities:
    # if cows and bulls count is zero all guess digits in all positions are impossible
    # if bulls count is zero all guess digits in current positions are impossible
    for position, digit in enumerate(guess_digits):
        if cows == 0 and bulls == 0:
            position_possible[:, digit] = False
        if bulls == 0:
            position_possible[position, digit] = False

guess_digits = None
while True:
    bulls, cows = [int(i) for i in input().split()]
    if bulls != -1:
        update_possible(correct_digits, position_possible, bulls, cows, guess_digits)
    guess_digits = random_possible_number(correct_digits, position_possible)
    print(''.join(map(str, guess_digits)))