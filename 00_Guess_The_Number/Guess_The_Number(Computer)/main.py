import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess < 1 or guess > x:
            print("out of range")
        elif guess < random_number:
            print("Sorry, guess again. Too Low.")
        elif guess > random_number:
            print("Sorry, guess again. Too High.")

    print(f"Yay, congrats. You have guess the number {random_number} correctly")



guess(20)