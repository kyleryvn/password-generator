import random


def generate(length):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '?', '#', '$', '%', '^', '&', '*']
    letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
               'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
               'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

    password_list = random.sample(numbers, 10)
    password_list += random.sample(symbols, len(symbols))
    password_list += random.sample(letters, len(letters))

    random.shuffle(password_list)
    password_list = random.sample(password_list, length)

    return "".join(char for char in password_list)


if __name__ == '__main__':
    print(f'Generated password: {generate(16)}')
