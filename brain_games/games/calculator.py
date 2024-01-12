from brain_games.games import utils


def create_random_expr():
    operations = ["+", "-", "*"]
    op = utils.random.choice(operations)
    left_num = utils.random.randint(1, 10)
    right_num = utils.random.randint(1, 10)
    return f"{left_num} {op} {right_num}"


def eval_expr(expression):
    left_num, op, right_num = expression.split()

    left = int(left_num)
    right = int(right_num)

    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right


def check_expression(result, answer, name):
    if result == answer:
        print("Correct!")
        return True

    else:
        print(
            f"'{answer}' is the wrong answer ;(. Correct answer was "
            f"'{result}'. \nLet's try again, {name}!"
        )
        return False


def play_calc():
    print("Welcome to the Brain Games!")
    user_name = utils.get_name()
    print(f"Hello, {user_name}!")
    print("What is the result of the expression?")
    win_game = True

    for i in range(3):
        expression = create_random_expr()
        print(f"Question: {expression}")
        user_answer = int(utils.prompt.string("Your answer: "))

        if not check_expression(eval_expr(expression), user_answer, user_name):
            win_game = False
            break

    if win_game:
        print(f"Congratulations, {user_name}!")
