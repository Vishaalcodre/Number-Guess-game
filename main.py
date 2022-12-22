#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

def high_or_low(n, guess, chances):
  if n > guess:
    print("Too low")
    return chances - 1
    

  elif n < guess:
    print("Too high")
    return chances - 1

  else:
    print(f"You got it right!, the answer is {n}")


chances = 0



def game():

  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  N = randint(1,100)
  
  lvl = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if lvl == 'easy':
    chances = 10

  else:
    chances = 5
    
  
  guess = 0
  
  while guess != N:

    print(f"You have {chances} attempts remaining to guess the number.\n")
    
    guess = int(input("Make a Guess: \n"))
    
    chances = high_or_low(N,guess,chances)

    if chances == 0:
      print("You've ran out of guesses, you lose.")
      return

    elif guess != N:
      print("Guess again")

game()