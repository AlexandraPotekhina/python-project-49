from brain_games.games.utils import generate_num, is_prime


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def evaluate():
    number = generate_num
    question = f"{number}"
    answer = str(is_prime(number))
    return (question, answer)
