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
