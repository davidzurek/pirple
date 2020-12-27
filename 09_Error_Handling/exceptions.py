
age_list = []
age_leftovers = []


def add_to_list():
    while len(age_list) != 5:
        try:
            age = int(input("Age: "))
            if age in age_list:
                age_leftovers.append(age)
            else:
                age_list.append(age)
        except ValueError as ex:
            print("You didn't enter a valid age.")
            print(ex)
            print(type(ex))
        finally:
            print("No exceptions were thrown.")
        print("Execution continues")


add_to_list()
print(age_list)
print(age_leftovers)
