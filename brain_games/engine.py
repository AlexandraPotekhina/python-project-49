from brain_games.cli import welcome_user
from brain_games.games.utils import get_answer


def check(result, answer, name):
    if result == answer:
        print("Correct!")
        return True

    else:
        print(
            f"'{answer}' is the wrong answer ;(. Correct answer was "
            f"'{result}'. \nLet's try again, {name}!"
        )
        return False


def play(game):
    user_name = welcome_user()
    print(game.RULE)
    win_game = True

    for i in range(3): #NUMBER_OF_ROUNDS = 3 in engine or utils
        question, correct_answer = game.evaluate()
        print(question)
        user_answer = get_answer()

        if not check(correct_answer, user_answer, user_name):
            win_game = False
            break

    if win_game:
        print(f"Congratulations, {user_name}!")