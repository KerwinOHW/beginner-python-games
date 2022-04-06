import random


def guess(x):
    random_number = random.randint(1, x)
    gue = 0
    while gue != random_number:
        gue = int(input(f"Guess a number between 1 and {x}: "))
        if gue < random_number:
            print('Sorry, guess again. Too low.')
        elif gue > random_number:
            print('Sorry, guess again. Too high.')

        print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            gue = random.randint(low, high)
        else:
            gue = low # could also be high
        feedback = input(f'Is {gue} too high (H), too low (L), or corrcet (C)??').lower()
        if feedback == 'h':
            high = gue - 1
        elif feedback == 'l':
            low = gue + 1

    print(f'Yay! The computer guessed your number, {x}, correctly!')


computer_guess(1000)
