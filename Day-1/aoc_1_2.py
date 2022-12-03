def main():
    most_calories = 0
    elves_packs = [[]]
    index = 0
    with open('aoc_1_input.txt', 'r') as iFile:
        reader = iFile.readlines()
        running_total = 0
        for line in reader:
            print(line.strip())
            if line.strip() != '':
                # running_total += int(line.strip())
                elves_packs[index].append(int(line.strip()))
            else:
                index += 1
                elves_packs.append([])
    elves_calories = [sum(pack) for pack in elves_packs]
    elves_calories.sort(reverse=True)
    print(elves_packs)
    print(elves_calories)
    print(sum(elves_calories[:3]))


if __name__ == '__main__':
    main()
