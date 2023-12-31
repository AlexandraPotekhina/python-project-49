import random
import prompt


def get_name():
    return prompt.string("May I have your name? ")


def get_answer():
    return prompt.string(f"Your answer: ")


def generate_num():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def find_gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    return number_1 + number_2
