# for the sake of this exercise the hangman figure will be created through loops and conditional statements

import random
from words import word_list
from termcolor import colored, cprint
from string import ascii_letters, ascii_uppercase
import time


def draw_hangman(head=False, body=False, left_arm=False, right_arm=False, left_leg=False, right_leg=False):
    for row in range(6):
        for col in range(7):
            if col == 6:
                print("")

            # gallow top bar
            if row == 0:
                if 1 < col < 6:
                    print("_", end="")
                else:
                    print(" ", end="")

            # gallow top bar support
            if row == 1:
                if col == 1 or col == 4:
                    print("|", end="")
                elif col == 2:
                    print("/", end="")
                else:
                    print(" ", end="")

            # head
            if row == 2:
                if col == 1:
                    print("|", end="")
                elif head == True and col == 4:
                    cprint("O", "red", end="")
                else:
                    print(" ", end="")

            # torso & arms
            if row == 3:
                if col == 1:
                    print("|", end="")
                elif body == True and col == 4:
                    cprint("|", "red", end="")
                elif left_arm == True and col == 3:
                    cprint("/", "red", end="")
                elif right_arm == True and col == 5:
                    cprint("\\", "red", end="")
                else:
                    print(" ", end="")

            # legs
            if row == 4:
                if col == 1:
                    print("|", end="")
                elif left_leg == True and col == 3:
                    cprint("/", "red", end="")
                elif right_leg == True and col == 5:
                    cprint("\\", "red", end="")
                else:
                    print(" ", end="")

            # gallow feet
            if row == 5:
                if col == 0:
                    print("/", end="")
                if col == 1:
                    print("\\", end="")
                else:
                    print(" ", end="")


def comitted_mistakes(mistakes):
    if mistakes == 0:
        draw_hangman(False, False, False, False, False, False)
    if mistakes == 1:
        draw_hangman(True, False, False, False, False, False)
    if mistakes == 2:
        draw_hangman(True, True, False, False, False, False)
    if mistakes == 3:
        draw_hangman(True, True, True, False, False, False)
    if mistakes == 4:
        draw_hangman(True, True, True, True, False, False)
    if mistakes == 5:
        draw_hangman(True, True, True, True, True, False)
    if mistakes == 6:
        draw_hangman(True, True, True, True, True, True)


def game_mode():
    answer = input(
        "Please select a game mode:\n A: VS Computer\n B: 2 Player Mode? \n").upper()
    if answer == "A":
        return answer
    elif answer == "B":
        return answer
    else:
        print("Please enter a valid value. Either 1 or 2\n")
        game_mode()


def get_word():
    word = random.choice(word_list)
    return word.upper()


def ask_for_word(repeat_text=None):
    question = repeat_text if repeat_text is not None else "Please enter your word.\n"
    word = input(question)
    if word.isalpha() == True and len(word) >= 3:
        return word.upper()
    else:
        return ask_for_word("Please enter at least 3 alphabets letters.\n")


def countdown():
    for t in reversed(range(1, 6)):
        timer = "{:02d}".format(t)
        print(f"{timer}", end="\r")
        time.sleep(1)


def play_again():
    answer = input("Do you wanna play again? (Y/N)\n").upper()
    if answer == "Y":
        main()
    elif answer == "N":
        print("Ok, see you.\n")
    else:
        print("Please enter a valid value. Either \"y\" or \"n\"\n")
        play_again()


def play():
    game_type = game_mode()
    if game_type == "A":
        word = get_word()
    else:
        word = ask_for_word()
    word_completion = ["_ " for char in word]
    word_completion_to_string = "".join(word_completion)
    guessed = False
    guessed_words = []
    guessed_letters = []
    mistakes = 0
    print("\nRemember your word. It will disappear in 5 seconds.")
    countdown()
    print(chr(27) + "[2J")
    comitted_mistakes(mistakes)
    print("\n")
    print(word_completion_to_string)
    print("\n")
    while not guessed and mistakes != 6:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter: {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                mistakes += 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_completion[index] = guess + " "
                word_completion_to_string = "".join(word_completion)
                if "_ " not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word: {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                mistakes += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion_to_string = word
        else:
            print("Not a valid guess.")
        print(chr(27) + "[2J")
        comitted_mistakes(mistakes)
        print("\n")
        print(word_completion_to_string)
        print("\n")
    if guessed:
        print("Congratulation, you guessed the word! You win!\n")
    else:
        print(
            f"Sorry, you ran out of tries. The word was: {word}. Maybe next time.\n")


def main():
    play()
    play_again()


main()
