from brain_games.games.utils import get_name


def welcome_user():
    print('Welcome to the Brain Games!')
    name = get_name()
    print(f'Hello, {name}!')
    return name
