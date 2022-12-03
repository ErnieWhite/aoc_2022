"""
"""
import os

def win_lose_draw(play: list)-> list:
    """Returns p so that we win/lose/draw
    :param play: list: [their play, our play]
    :return: list
    """
    wins = {'S': 'R', 'R': 'P', 'P': 'S'}
    loses = {v: k for k, v in wins.items()}
    # do we need to have a draw game?
    if play[1] == 'D':
        play[1] = play[0]
        return play

    # do we need to win this one?
    if play[1] == 'W':
        play[1] = wins[play[0]]
        return play

    # we need to lose this one
    play[1] = loses[play[0]]

    return play


def win_lose_draw_score(play):
    """Returns the score for the win/lose/draw"""

    wins = [['S', 'R'], ['R', 'P'], ['P', 'S']]

    if play[0] == play[1]:
        return 3

    if play in wins:
        return 6

    return 0


def round_score(play):
    """Returns the total score of the round"""

    choice_score = {'R': 1, 'P': 2, 'S': 3}
    play = win_lose_draw(play)
    return choice_score[play[1]] + win_lose_draw_score(play)


def main():
    print(os.getcwd())
    rounds = []
    scores = []
    conversion = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'L', 'Y': 'D', 'Z': 'W'}
    with open('Day-2/data/input.txt', 'r', encoding='utf-8') as data_file:
        reader = data_file.readlines()
        for line in reader:
            rounds.append(line.strip().split(' '))

            rounds[-1][0] = conversion[rounds[-1][0]]
            rounds[-1][1] = conversion[rounds[-1][1]]

            scores.append(round_score(rounds[-1]))
            print(rounds[-1])
    print(scores)
    print(sum(scores))


if __name__ == '__main__':
    print(os.getcwd())
    main()
