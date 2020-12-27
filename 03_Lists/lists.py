my_unique_list = []
my_leftovers = []


def add_to_list(input1):
    if input1 in my_unique_list:
        return my_leftovers.append(input1)
    return my_unique_list.append(input1)


add_to_list(1)
add_to_list(2)
add_to_list("three")
add_to_list("three")


print(f"My Unique List: {my_unique_list}")
print(f"My Leftovers: {my_leftovers}")
