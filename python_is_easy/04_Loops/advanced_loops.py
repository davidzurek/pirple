def playing_board(rows, columns):
    if type(rows) != int and type(columns) != int:
        print("Please enter an int value.")
        return False

    if rows <= 1 or columns <= 1:
        print("Values must be equal or greater than 3.")
        return False

    if rows % 2 == 0 or columns % 2 == 0:
        print("Values must be odd.")
        return False

    if rows > 51 or columns > 121:
        print("Values out of range. Please enter a valid value.\n Max. row: 51, max. columns: 121.")
        return False

    else:
        for row in range(rows):
            if row % 2 == 0:
                for column in range(columns):
                    if column % 2 == 0:
                        print(" ", end="")

                        if column == columns-1:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)


playing_board(9, 9)
