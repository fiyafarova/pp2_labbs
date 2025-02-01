def GuessTheNumber():
    import random
    number = random.randint(1,20)
    guesscnt = 0
    name = input('Hello! What is your name?\n')
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')
    guess = 0

    while(guess != number ):
        guess = int(input())
        guesscnt+=1
        if guess < number:
            print('Your guess is too low.\n')
        elif guess > number:
            print('Your guess is too high.\n')
    print(f'Good job, {name}! You guessed my number in {guesscnt} guesses!')

GuessTheNumber()