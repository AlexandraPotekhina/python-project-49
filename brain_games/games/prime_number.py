from brain_games.games.utils import generate_num, is_prime


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def evaluate():
    number = generate_num()
    question = f"Question: {number}"
    answer = 'yes' if is_prime(number) else 'no'
    return (question, answer)
