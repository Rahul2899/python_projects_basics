# Random number generated
# a loop should run 5 times to user giving 5 tries
# if the user guessess the number outside specified range -> issue a warning
# if user guess the  number right terminate loop
# if the number is wrong then continue
# define a function that guide the user



# Importing random library

import random 

def guess(rand_int):
    guess_int = int(input("enter the number:"))
    if guess_int > 100 or guess_int < 0:
        print("Number out of range")
    if guess_int > rand_int:
        print("Try smaller number")
    elif guess_int < rand_int:
        print("Try larger number ")
    elif guess_int == rand_int:
        return 'Match'

rand_int = random.randint(0,100)
print("You will get 5 tries to guess the number (0-100)")

flag = 0
for i in range(0,5):
    ans = guess(rand_int)
    if(ans == ' Match'):
        flag = 1
        break
if(flag == 1):
    print("congratlations you got it right")

else:
    print("Try again later and your correct answer was: ",rand_int)

    