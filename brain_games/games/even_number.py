from brain_games.games.utils import generate_num, is_even


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

def evaluate():
    number = generate_num()
    question = f"{number}"
    answer = 'yes' if is_even(number) else 'no'
    return (question, answer)
