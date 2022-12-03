def win(p):
    wins = [['S', 'R'], ['R', 'P'], ['P', 'S']]
    if p[0] == p[1]:
        return 3
    if p in wins:
        return 6
    else:
        return 0


def round_score(p):
    choice_score = {'R': 1, 'P': 2, 'S': 3}
    return choice_score[p[1]] + win(p)


def main():
    rounds = []
    scores = []
    with open('data/input.txt', 'r') as f:
        reader = f.readlines()
        for line in reader:
            rounds.append(line.strip().split(' '))
            if rounds[-1][0] == 'A':
                rounds[-1][0] = 'R'
            if rounds[-1][0] == 'B':
                rounds[-1][0] = 'P'
            if rounds[-1][0] == 'C':
                rounds[-1][0] = 'S'
            if rounds[-1][1] == 'X':
                rounds[-1][1] = 'R'
            if rounds[-1][1] == 'Y':
                rounds[-1][1] = 'P'
            if rounds[-1][1] == 'Z':
                rounds[-1][1] = 'S'

            scores.append(round_score(rounds[-1]))
            print(rounds[-1])
    print(scores)
    print(sum(scores))


if __name__ == '__main__':
    main()
