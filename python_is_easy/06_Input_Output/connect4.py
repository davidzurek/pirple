# for the sake of this exercise the boad matrix has been created "manually".

import sys
from termcolor import colored, cprint


def draw_field(field):
    for row in range(11):
        if row % 2 == 0:
            practical_row = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    praticial_column = int(column / 2)
                    if column != 12:
                        print(field[praticial_column][practical_row], end="")
                    else:
                        print(field[praticial_column][practical_row])
                else:
                    print("|", end="")

        else:
            print("-" * 13)


def is_valid_field(current_field, move_column):
    return current_field[move_column][0] == " "


def next_field(current_field, move_column):
    for r in reversed(range(6)):
        if current_field[move_column][r] == " ":
            return r


def winning_move(current_field, piece):
    # horizontal
    for move_column in range(4):
        for r in range(6):
            if current_field[move_column][r] == print_color(piece) and current_field[move_column+1][r] == print_color(piece) and current_field[move_column+2][r] == print_color(piece) and current_field[move_column+3][r] == print_color(piece):
                return True

    # vertical
    for move_column in range(7):
        for r in range(3):
            if current_field[move_column][r] == print_color(piece) and current_field[move_column][r+1] == print_color(piece) and current_field[move_column][r+2] == print_color(piece) and current_field[move_column][r+3] == print_color(piece):
                return True

    # positive diagonal
    for move_column in range(4):
        for r in range(3):
            if current_field[move_column][r] == print_color(piece) and current_field[move_column+1][r+1] == print_color(piece) and current_field[move_column+2][r+2] == print_color(piece) and current_field[move_column+3][r+3] == print_color(piece):
                return True

    # negative diagonal
    for move_column in range(4):
        for r in range(3, 6):
            if current_field[move_column][r] == print_color(piece) and current_field[move_column+1][r-1] == print_color(piece) and current_field[move_column+2][r-2] == print_color(piece) and current_field[move_column+3][r-3] == print_color(piece):
                return True


def print_color(piece):
    if piece == "x":
        return colored(piece, "white", "on_red")
    else:
        return colored(piece, "white", "on_yellow")


def start_game():
    current_field = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [
        " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
    draw_field(current_field)
    player = 1
    game_over = False
    while not game_over:
        print(f"Players turn: {player}")
        move_column = int(input("Please select a column (0-6)\n"))
        if move_column > 6:
            print("Sorry, value is out of range. Please enter a valid number")
            continue
        else:
            move_row = next_field(current_field, move_column)

        if player == 1:
            if is_valid_field(current_field, move_column):
                if current_field[move_column][move_row] == " ":
                    current_field[move_column][move_row] = print_color("x")

                if winning_move(current_field, "x"):
                    print("Congrats, you've won the game!")
                    draw_field(current_field)
                    game_over = True
                    print("Do you wanna play again? Y/N\n")
                    while game_over:
                        restart = input("")
                        if restart.lower() == "y":
                            start_game()
                            break
                        if restart.lower() == "n":
                            print("See you.")
                            break
                        else:
                            print("Please enter a valid input. Y/N\n")
                            continue
                    break

            else:
                print("Oops. Invalid field. Please select another column.")

            player = 2
            draw_field(current_field)

        else:
            print(f"Players turn: {player}")

            if is_valid_field(current_field, move_column):
                if current_field[move_column][move_row] == " ":
                    current_field[move_column][move_row] = print_color("o")

                if winning_move(current_field, "o"):
                    print("Congrats, you've won the game!")
                    draw_field(current_field)
                    game_over = True
                    print("Do you wanna play again? Y/N\n")
                    while game_over:
                        restart = input("")
                        if restart.lower() == "y":
                            start_game()
                            break
                        if restart.lower() == "n":
                            print("See you.")
                            break
                        else:
                            print("Please enter a valid input. Y/N\n")
                            continue
                    break
            else:
                print("Oops. Invalid field. Please select another column.")

            player = 1
            draw_field(current_field)


start_game()
