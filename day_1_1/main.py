def main():
    with open('input.txt', 'r') as iFile:
        reader = iFile.readlines()
        for line in reader:
            print(line)

if __name__ == '__main__':
    main()

