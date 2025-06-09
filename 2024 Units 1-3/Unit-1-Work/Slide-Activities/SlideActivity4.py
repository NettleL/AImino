import random

print('')

guesses = 0

number = random.randint(1,4)
name = input("Hello! What is your name? ")

print("Well,", name + "! I am thinking of a number between 1 and 20.")
print('Take a guess.')
guess = int(input())
    
while guess != number:
    while guesses < 6:
        if guess < number:
            print('Your guess is too low.')
            guesses = guesses + 1
            print(str(guesses), 'guesses')
            print('Take a guess.')
            guess = int(input())
        if guess > number:
            print('Your guess is too high.')
            guesses = guesses + 1
            print(str(guesses), 'guesses')
            print('Take a guess.')
            guess = int(input())
        if guess == number:
            guesses = guesses + 1
            print(str(guesses), 'guesses')
            break
    break

if guess == number:
    if guesses == 0:
        guesses = guesses + 1 #when guess is gotten on the first try, the while loop does not occur and therefore the first guess is not added. This fixes that :)
    print("Yay! you got it! Congratulations! It only took " + str(guesses) + " guesses!")
    
else:
    numberstring = str(number)
    print(" :( The number was " + numberstring)
    
print('')
