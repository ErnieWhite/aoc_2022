def main():
    most_calories = 0
    with open('aoc_1_input.txt', 'r') as iFile:
        reader = iFile.readlines()
        running_total = 0
        for line in reader:
            print(line.strip())
            if line.strip() != '':
                running_total += int(line.strip())
            else:
                if running_total > most_calories:
                    most_calories = running_total
                running_total = 0
    print(f'\nmax: {most_calories}')


if __name__ == '__main__':
    main()

