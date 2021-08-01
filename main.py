for number in range(1, 1000000):
    if set(list(str(2 * number))) == set(list(str(3 * number))) == set(list(str(4 * number))) == set(list(str(5 * number))) == set(
            list(str(6 * number))):
            print(number)
