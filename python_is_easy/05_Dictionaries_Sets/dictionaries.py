song_information = dict(
    title="Make It Better",
    artist="Anderson Paak",
    featured_artist="Smokey Robinson",
    genre="R&B/Soul",
    duration_sec=220,
    release_year=2019)

for i in song_information:
    print(f"{i}: {song_information[i]}")


def guess_song_info(key, value):
    return song_information[key].lower() == value.lower()


def inputs():
    input_key = input("\nGreat! Can you guess the key?\n")
    input_value = input(
        f"\nNow, what do you think is the value for {input_key}?\n")
    input_key = input_key.lower()
    input_value = input_value.lower()
    if input_key in song_information and guess_song_info(input_key, input_value) == True:
        print(
            f"\nCongratulations! You've guessed {input_value} to {input_key} correctly.\nDo you want to play again? Y/N")
        while True:
            try_again = input("")
            if try_again.lower() == "y":
                inputs()
                break
            elif try_again.lower() == "n":
                print("\nSee you.\n")
                break
            else:
                print("\nPlease enter a valid value.\n")
    else:
        print(f"\nUnfortunately you've missed. Try again? Y/N\n")
        while True:
            try_again = input("")
            if try_again.lower() == "y":
                inputs()
                break
            elif try_again.lower() == "n":
                print("\nSee you.\n")
                break
            else:
                print("\nPlease enter a valid value.\n")


def start_game():
    print("\nDo you want to start the guessing game? Y/N\n")
    while True:
        start = input("")
        if start.lower() == "n":
            print("\nOk, see you next time.\n")
            break

        elif start.lower() == "y":
            inputs()

        else:
            print("\nPlease enter a valid value.\n")
        break


start_game()
