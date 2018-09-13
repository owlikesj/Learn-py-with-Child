import random

secret = random.randint(1, 100)
guess = 0
tries = 0

while guess != secret and tries < 6:
    guess = input("what's your guess? ")
    if guess < secret:
        print "Too low, try again!"
    elif guess > secret:
        print "Too high, try again!"
    tries = tries + 1

if guess == secret:
    print "Great! You got it!"
else:
    print "No more guess! Better luck next time."
    print "The secret number was", secret

    
