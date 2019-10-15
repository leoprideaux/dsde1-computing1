# I will be making a game where there is a random number that must be
# guessed by the user. A correct guess will end the game.

import random

# enter name and begin
print('Hello, welcome to the number guessing game!')

print('What is your name?')
playername = input()
print('Hi ' + playername + '! let us begin...')

#random number generation
randnbr = random.randint(1,10)

# user selects random number
print('Let me think...')
print('I have a number in mind... It is between 1 and 10')
print('Have a guess... Take your time, make it good.')
guess = input()
# convert the number the user has inputted into a integer so that it can 
# be compared to the computer's number
guess = int(guess)

# compare guess to computer's number and determine whether it is the same
if guess == randnbr:
    print('Agh! First try?! You lucky bugger')
    sys.exit()
else:
    print('you fool. you absolute moron. you are such a monumental idiot that you dont even realize what you just said. i am a verbal magician and you, my friend, are a naive simpleton.')
    print('...')
    print('but...')
    print('Im feeling nice, guess again')
    guess = input()
    guess = int(guess)
    
