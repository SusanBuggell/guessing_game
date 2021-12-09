# A number-guessing game.

# print('hi')

import random

# greet player and get player name
user_name= input('Greetings. What is your name?\n')

#tell user about the game
print(f'\n{user_name}, I am thinking of a number between 1 and 100.\n')

# computer defines a random number between 1-100
comp_rng=random.randint(1,100)

#define lower and upper boundaries based on range and/or guesses
lower_bound=0
upper_bound=100

# promput user for initial guess
user_guess=input('Your guess?\n') 

guesses=1

guess_is_int = False
guess_in_bounds = False


def is_int():
    """Is user input an int?"""
    global user_guess
    global guesses
    global guess_is_int

    while type(user_guess)!=int:

        #Is user_guess an integer?
        try:
            user_guess=int(user_guess)
            print(f'{type(user_guess)} {user_guess}')
            guess_is_int = True
            break
        
        except ValueError:
            print(f'Really {user_name}?!?!?!?! {user_guess} is not even close to an integer.')
            user_guess=input('Do you want to maybe try entering an integer?\nYour guess?\n')
            guesses += 1
           # print(f'{guesses} tries')
    return guess_is_int
    
help(is_int)