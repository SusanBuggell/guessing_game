# A number-guessing game.

import random
from colorama import Fore
from colorama import Style

# greet player and get player name
user_name= input(f'{Fore.CYAN}Greetings and salutations. What is your name?{Style.RESET_ALL}\n')

#tell user about the game
print(f'{Fore.LIGHTGREEN_EX}{user_name}, I am thinking of a number between 1 and 100.')

#define lower and upper boundaries based on range and/or guesses
lower_bound=1
upper_bound=100

# computer defines a random number between 1-100
comp_rng=random.randint(lower_bound,upper_bound)

# promput user for initial guess
user_guess=input(f'Your guess?{Style.RESET_ALL} \n') 

guesses=1

guess_is_int = False
guess_in_bounds = False


# def is_int():
#     """Is user input an int?"""
#     global user_guess
#     global guesses
#     global guess_is_int

#     while type(user_guess)!=int:

#         #Is user_guess an integer?
#         try:
#             user_guess=int(user_guess)
#             print(f'{type(user_guess)} {user_guess}')
#             guess_is_int = True
#             break
        
#         except ValueError:
#             print(f'Really {user_name}?!?!?!?! {user_guess} is not even close to an integer.')
#             user_guess=input('Do you want to maybe try entering an integer?\nYour guess?\n')
#             guesses += 1
#            # print(f'{guesses} tries')
#     return guess_is_int
    
# help(is_int)

def is_int():
  """Is user input an int?"""
  global user_guess
  global guesses

  try:
    user_guess=int(user_guess)
    return True
  except ValueError: 
    print(f'{Fore.LIGHTRED_EX}Really {user_name}?!?!?!?! {user_guess} is not even close to an integer.')
    while isinstance(user_guess, int) == False:
      user_guess = input(f'Do you want to maybe try entering an integer?\nYour guess?{Style.RESET_ALL} \n')
      guesses += 1
      is_int()

# help(is_int)
# is_int()

# Is user_guess between the upper and lower bounds?
def in_bounds():

  global user_guess
  global lower_bound
  global upper_bound
  global guesses 

  is_int()

  while user_guess < lower_bound or user_guess > upper_bound:
    print(f'{Fore.LIGHTRED_EX}Come on!!!! {user_guess} is clearly not between {lower_bound} and {upper_bound}.\nHow about trying an integer between {lower_bound} and {upper_bound}, huh?')
    user_guess=input(f'Your guess? {Style.RESET_ALL}\n')
    guesses += 1
    is_int()
    in_bounds()


  return True

in_bounds()

while user_guess>comp_rng or user_guess<comp_rng: 
  if user_guess>comp_rng:
      upper_bound=user_guess-1
      user_guess=input(f'{Fore.MAGENTA}Your guess is too high. Try again.\nYour guess?{Style.RESET_ALL}\n')
      guesses += 1
      is_int()
      in_bounds()
  elif user_guess<comp_rng:
        lower_bound=user_guess+1
        user_guess=input(f'{Fore.LIGHTBLUE_EX}Your guess is too low. Try again.\nYour guess?{Style.RESET_ALL}\n')
        guesses += 1
        is_int()
        in_bounds()
if user_guess==comp_rng:
  if guesses==1:
    print(f'/{Fore.LIGHTGREEN_EX}You are amazing, {user_name}. My number was {comp_rng}.  You  must be a mind reader. You guessed it in {guesses} try.{Style.RESET_ALL}')
  elif guesses>1:
    print(f'{Fore.GREEN}Congratulations {user_name}, my number was {comp_rng}.  You guessed it in {guesses} tries.{Style.RESET_ALL}')

# # Is user_guess > comp_rng?
# def too_high():

#     global comp_rng
#     global user_guess
#     global upper_bound
#     global lower_bound
#     global guesses

#     while user_guess > comp_rng:
#         upper_bound=user_guess            
#         user_guess=input(f'Your guess is too high. Enter a guess between {lower_bound} and {upper_bound}.  \n Your guess?\n')
#         guesses +=1
#     return True

# # guess_not_high=too_high()

# # Is user_guess > comp_rng?
# def too_low():
#     global comp_rng
#     global user_guess
#     global upper_bound
#     global lower_bound
#     global guesses

#     while user_guess < comp_rng:
#         lower_bound=user_guess
#         user_guess=input(f'Your guess is too low, Enter a guess between {lower_bound} and {upper_bound}.\n Your guess?\n')
#         guesses +=1   
#     return True      

# # guess_not_low=too_low()



# while comp_rng!=user_guess:
  
#     while guess_is_int == False or guess_in_bounds == False or guess_not_high == False or guess_not_high == False :
#         if guess_is_int == True:
#             if guess_in_bounds == True:
#                 if guess_not_high == True:
#                     if guess_not_low == True:
#                         break
#                     else: too_low()
#                 else: too_high()    
#             else: in_bounds()
#         else: is_int()

# if (comp_rng==user_guess):
#         print(f'Congratuations, {user_name}! You won. It took you {guesses} tries to guess {comp_rng}.')