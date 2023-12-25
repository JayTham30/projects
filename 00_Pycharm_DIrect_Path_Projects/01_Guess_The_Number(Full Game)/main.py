import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}\n"))
        if guess > x:
            print(f"Invalid number please pick a number in the range of 1 and {x}.")
        elif guess > random_number:
            print("Too High")
        elif guess < random_number:
            print("Too Low")

    print(f"Yay you have correctly guessed {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    print(f"Think of a number between 1 and {x}")

    while feedback != 'c':
        if low != high:
            random_number = random.randint(low, high)
        else:
            random_number = high
        feedback = input(f"Is {random_number} too high (H), too low (l), or correct (c)?\n").lower()
        if feedback == "h":
            high = random_number - 1
        elif feedback == "l":
            low = random_number + 1
        elif feedback != "c" or "h" or "l":
            print('Invalid Answer. Please input "c", "h", or "l"')

    print(f"I win! I've guessed {random_number}!!")


try:
    guess(100)

    play_next = input("Now it's my turn! Do you want to play? type in (YES) or (NO).\n").lower()
    if play_next == "yes":
        computer_guess(1000)
    elif play_next == "no":
        print("Goodbye!")

except:
    print("Invalid Input")
