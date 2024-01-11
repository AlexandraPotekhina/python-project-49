import random
import prompt
import math


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



def generate_progression():
    regression = [random.randint(1, 10)]
    rand_num = random.randint(1, 5)

    for i in range(11):
        regression.append(regression[i] + rand_num)

    missing_number = random.choice(regression)
    index = regression.index(missing_number)
    regression[index] = '..'

    return (regression, missing_number)


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

