# Number guessing game

import random


def run_game(lower_bound, upper_bound, num_guesses):
    target_number = random.randint(lower_bound, upper_bound)
    for n in range(num_guesses):
        guess = int(input('Enter your guess: '))
        if guess == target_number:
            print("You win!")
            break
        elif guess < target_number:
            print("Your guess was too low, please try again!")
        elif guess > target_number:
            print("Your guess was too high, please try again!")


if __name__ == '__main__':
    run_game(1, 10, 5)

