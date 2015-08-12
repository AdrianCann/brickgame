import random

guessesTaken = 0

print("Hello human, what is your name?")
myName = raw_input()

number = random.randint(1, 50)
print ("Well, fleshing called- " + myName + ", I am thinking of a number between 1 and 50. You have 10 tries to guess the number correctly.")

while guessesTaken < 10:
    print ("Please... try me.. guess the number I am thinking of")
    guess = int(raw_input())
    count = str(guessesTaken + 1)
    if count == "1":
        print ("You have taken " + count + " guess thus far")
    else:
        print ("Oops, you have taken " + count + " guesses thus far")

    guessesTaken = guessesTaken + 1

    if guess < number:
        print ("Your guess is too low!")

    if guess > number:
        print ("Your guess is too high!")

    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print ("Good job, " + myName + "! You guessed my number in " + guessesTaken + \
        " guesses" )
if guess != number:
    number = str(number)
    print ("Nope. The number I was thinking of was " + number)
