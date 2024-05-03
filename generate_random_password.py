import string
import random

all_characters = string.ascii_letters + string.digits + string.punctuation


def main():
    # code for the main function
    print(generate_random_password(20, 10, True, True))


def generate_random_password(length, count, digits, spl_chars):
    passwords = []
    all_chars = string.ascii_letters
    if digits:
        all_chars = all_chars + string.digits

    if spl_chars:
        all_chars = all_chars + string.punctuation

    for i in range(count):
        password = ''.join(
            random.choice(all_chars) for _ in range(length))
        passwords.append(password)
    return passwords


if __name__ == "__main__":
    main()
