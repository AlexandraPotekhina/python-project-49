from brain_games.games.utils import generate_progression


RULE = 'What number is missing in the progression?'

def evaluate():
    progression, missing_number = generate_progression()
    question = f"{' '.join(map(str, progression))}"
    answer = str(missing_number)
    return (question, answer)
