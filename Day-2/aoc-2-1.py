def win(play):
    wins = [['S', 'R'], ['R', 'P'], ['P', 'S']]
    if play[0] == play[1]:
        return 3
    if play in wins:
        return 6
    else:
        return 0


def round_score(play):
    choice_score = {'R': 1, 'P': 2, 'S': 3}
    return choice_score[play[1]] + win(play)


def main():
    rounds = []
    scores = []
    conversion = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
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
    main()
