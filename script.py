"""
Name: Dennis Kamau
Phone: 0759360020
Email: dmkamau475@gmail.com
Website: www.denmau.me
"""


def validate_input(n, scores):
    # check if n is a valid integer
    try:
        n = int(n)
    except ValueError:
        print("Number of participants should be a valid number")
        return False

    # Number of participants should gretaer or equal to 2 and less than or equal to 10
    if n < 2 or n > 10:
        print("Number of participants should be greater or equal to 2 and less than or equal to 10")
        return False

    # check if scores are valid integers
    try:
        # split score by space and cast to int list
        scores = list(map(int, scores.split()))
    except ValueError:
        print("Scores must be integers separated by space")
        return False

    # check if the number of scores is equal to n
    if len(scores) != n:
        print("Number of scores must be equal to number of participants")
        return False

    # check if each number in scores is greater than or equal to -100 and less than or equal to 100
    if not all(score >= -100 and score <= 100 for score in scores):
        print("Scores must be greater than or equal to -100 and less than or equal to 100")
        return False

    return True


def find_runner_up_score(scores):

    # sort and remove duplicates
    scores = sorted(set(scores))
    # find the second highest score
    return scores[-2]


if __name__ == '__main__':
    """ 
        gets the number of participants, and a scoresheet then returns the second highest score 
    """
    # get the first line of parameters (n - number of participants)
    n = input('enter number of participants, n: $')

    # try to cast n to int and see if it is valid
    try:
        n = int(n)
    except ValueError:
        print('n must be an integer')
        exit(1)

    # get the scores as a string of numbers separated by space
    scores = input('enter scores separated by space: $')

    if validate_input(n, scores):
        # call the function and print the result
        print(f'runner-up score is {find_runner_up_score(scores)}')
    else:
        exit(1)
