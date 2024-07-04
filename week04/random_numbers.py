### Author: Adson Mettler do Nascimento

"""
Write and call functions that demonstrate both
default parameter values and pass by reference.
"""

import random

def main():
    
    print()
    numbers = [16.2, 75.1, 52.3]
    print(f"Numbers: {numbers}")
    
    print()
    append_random_numbers(numbers)
    print(f"Numbers: {numbers}")

    print()
    append_random_numbers(numbers, 3)
    print(f"Numbers: {numbers}")

    print()

    words = []

    append_random_words(words)
    print(f"Words: {words}")

    print()
    append_random_words(words, 3)
    print(f"Words: {words}")

    print()


def append_random_numbers(numbers_list, quantity=1):

    for x in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity=1):

    objects = ["smartphone", "laptop", "bottle", "mouse", "cookie", "window", "chair", "keyboard", "wallet"]

    for x in range(quantity):
        random_word = random.choice(objects)
        words_list.append(random_word)

    
if __name__ == "__main__":
    main()


