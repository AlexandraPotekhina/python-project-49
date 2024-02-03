from brain_games.games import utils


def check_answer(number, answer, name):
    if (
        (utils.is_prime(number) and (answer == 'yes'))
        or (not utils.is_prime(number) and (answer == 'no'))
    ):
        print("Correct!")
        return True

    else:
        print(
            f"'{answer}' is the wrong answer ;(. Correct answer was "
            f"'{'yes' if utils.is_prime(number) else 'no'}'. \nLet's try again, "
            f"{name}!"
        )
        return False


def play_prime():
    print('Welcome to the Brain Games!')
    user_name = utils.get_name()
    print(f"Hello, {user_name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    win_game = True

    for i in range(3):
        number = utils.generate_num()
        print(f"Question: {number}")
        user_answer = utils.get_answer()

        if not check_answer(number, user_answer, user_name):
            win_game = False
            break

    if win_game:
        print(f"Congratulations, {user_name}!")
