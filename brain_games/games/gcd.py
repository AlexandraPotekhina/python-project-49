from brain_games.games.utils import generate_num, find_gcd


RULE = 'Find the greatest common divisor of given numbers.'

def evaluate():
    num1 = generate_num()
    num2 = generate_num()
    question = f"{num1} {num2}"
    answer = str(find_gcd(num1, num2))
    return (question, answer)
