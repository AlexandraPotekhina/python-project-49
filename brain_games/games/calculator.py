import operator
from random import choice
from brain_games.games.utils import generate_num


RULE = 'What is the result of the expression?'


operations = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul
              }

def evaluate():
    operation = choice(list(operations.keys()))
    num1 = generate_num()
    num2 = generate_num()
    question = f"Question: {num1} {operation} {num2}"
    answer = str(operations[operation](num1, num2))
    return (question, answer)
