from brain_games.games import utils


def check_answer(number_1, umber_2, answer, name):
    if utils.find_gcd(number_1, number_2) == answer:
        print("Correct!")
        return True

    else:
        print(
            f"'{answer}' is the wrong answer ;(. Correct answer was "
            f"{utils.find_gcd(number_1, number_2}. \nLet's try again, " 
            f"{name}!"
        )
        return False


def play_game():
    print('Welcome to the Brain Games!')
    user_name = utils.get_name()
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
    win_game = True

    for i in range(3):
        number_1 = utils.generate_num()
        number_2 = utils.generate_num()
        print(f"Question: {number_1, number_2}")
        user_answer = utils.get_answer()

        if not check_answer(number_1, number_2, user_answer, user_name):
            win_game = False
            break

    if win_game:
        print(f"Congratulations, {user_name}!")
