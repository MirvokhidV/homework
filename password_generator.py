import random
import string


def password_decorator(func):
    def wrapper(length):
        password = func(length)
        return password + str(random.randint(0, 100))
    return wrapper


@password_decorator
def generate_password(length):
    permission = {}
    characters = string.ascii_letters + string.digits + string.punctuation
    print(
        "To generate passwords we have some changes, choose them [write them in one line, f.e. {1 2 3}]")
    print("1. Letters\n2. Digits\n3. Punctuations")
    answer = list(map(int, input().split()))
    for i in answer:
        if i == 1:
            permission['letters'] = 1
            characters += string.ascii_letters
        elif i == 2:
            permission['digits'] = 1
            characters += string.digits
        elif i == 3:
            permission['punctuations'] = 1
            characters += string.punctuation
    password = "".join(random.sample(characters, length))
    return password


print(generate_password(int(input("Enter the length of the code: "))))
