import random

def guess(x):
    random_number =  random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess an number between 1 and {x}: "))

        if guess < random_number:
            print('Sorry, guess again. Your number is too low.')
        elif guess > random_number:
            print('Sorry guess again. Your number is too high.')
    
    print(f'Good job! You got the correct answer: {random_number}')

guess(50)