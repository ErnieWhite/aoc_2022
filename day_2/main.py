
def main():
    with open('data/input.txt', 'r') as f:
        reader = f.readlines()
        for line in reader:
            print(line.strip())


if __name__ == '__main__':
    main()
