#banana.py
## by: Roy Lee

import time
from string import ascii_lowercase
from random_word import RandomWords

## get number of attempts
def get_num_attempts():
    while True:
        num_attempts = input("How many number of attempts would you like?")

        try:
            num_attempts = int(num_attempts)
            if num_attempts >= 1:
                return num_attempts
            else:
                print("You need at least one attempt haha")
        except ValueError:
            print("{0} is not a valid number".format(num_attempts))

## get word length
def get_word_length():
    while True:
        word_length = input("What word length would you like? (MIN: 4, MAX: 10)")

        try:
            word_length = int(word_length)
            if 4 <= word_length <= 10:
                return word_length
            else:
                print("Follow the instructions please tyty :)")
        except ValueError:
            print("{0} is not a valid number".format(word_length))

## get guessed letter
def get_guess_letter():
    print("guessed letters:", end ="")
    print(guessed_letters)
    while True:
        guess_letter = input("guess a letter any letter")
        if len(guess_letter) != 1:
            print("enter ONE letter buddy")
        elif guess_letter not in ascii_lowercase:
            print("that is not a letter >:(")
        elif guess_letter in guessed_letters:
            print("you guessed that letter already")
        else:
            guessed_letters.append(guess_letter)
            return guess_letter

## replace letter in display_word
def replace_letter(string, letter, index):
    return string[:index] + letter + string[index + 1:]

## ask if player wants to play again
def play_again():
    while True:
        print('''


                ''')
        answer = input("play again? (y/n)")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("y or n only pls")

## game loop
playing = True
while playing == True:
    print("Hey play my game of hangman pls tysm")
    print("           by: Roy Lee")
    print(" ") ## for spacing

    num_attempts = get_num_attempts()
    word_length = get_word_length()
    guessed_letters = []

    print(" ") ## for spacing

    w = RandomWords()
    randomword = w.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minLength=word_length, maxLength=word_length)
    word = str(randomword).lower()

    display_word = "_" * (word_length)

    print("Loading game...")
    time.sleep(1)
    print("Done in a sec...")
    time.sleep(1)
    print("Play!")

    while num_attempts > 0:
        ## for spacing
        print('''


        ''')
        print(display_word)
        print(str(num_attempts) + " attempts left")
        guess_letter = get_guess_letter()

        if guess_letter in word:
            print("yay gj you gussed the right letter :)")

            i = 0
            while i < len(word):
                if word[i] == guess_letter:
                    display_word = replace_letter(display_word, guess_letter, i)
                i = i + 1

        else:
            print("oops that is wrong :(")
            num_attempts = num_attempts - 1

        if display_word == word:
            ## for spacing
            print('''


            ''')
            print("yay you won!!!")
            break

    if num_attempts == 0:
        ## for spacing
        print('''


            ''')
        print("you lost... nice try :(")
    time.sleep(1)
    print("the word was: " + str(word))

    if play_again():
        playing = True
    else:
        playing = False
        quit()
