def random_func(input1, input2, input3):
    if input1 == input2 and input1 == input3:
        return True
    return False


print(random_func(1, 1, 1))
print(random_func(1, 2, 3))
print(random_func(1, 1, int("1")))
