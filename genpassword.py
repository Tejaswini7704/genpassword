import string
import random
def g_p(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 or more to include all character types.")

    lowercases = string.ascii_lowercase
    uppercases = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation 

    password = [
        random.choice(lowercases),
        random.choice(uppercases),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_characters = lowercases + uppercases + digits + special_chars
    password += [random.choice(all_characters) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the length of the password:"))

        password = g_p(length)
        print("The Generated Password:", password)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()