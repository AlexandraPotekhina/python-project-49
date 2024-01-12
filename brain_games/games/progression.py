from brain_games.games import utils


def check_answer(number, answer, name):
    if str(number) == answer:
        print("Correct!")
        return True

    else:
        print(
            f"'{answer}' is the wrong answer ;(. Correct answer was "
            f"'{number}'. \nLet's try again, "
            f"{name}!"
        )
        return False


def play_progression():
    print('Welcome to the Brain Games!')
    user_name = utils.get_name()
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    win_game = True

    for i in range(3):
        progression, number = utils.generate_progression()
        print(f"Question: {', '.join(map(str, progression))}")
        user_answer = utils.get_answer()

        if not check_answer(number, user_answer, user_name):
            win_game = False
            break

    if win_game:
        print(f"Congratulations, {user_name}!")
