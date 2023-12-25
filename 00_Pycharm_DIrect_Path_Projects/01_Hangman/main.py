import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a words from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guessed

    lives = int(lives_feedback)


    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #Letters used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'left and you have used these letters: ', ' '.join(used_letters))

        #What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter == "give up":
            print(f"You gave up! the word was {word}.")

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away life if wrong
                print('Letter is not in word.')




        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    #Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, Sorry. The word was', word)

    else:
        print('You guessed the word', word, 'correct!!')

lives_feedback = input(f"How many lives would to play with? \n")

hangman()
