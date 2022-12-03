def main():
    """ read the file
    """

with open('input.txt') as f:
    [print(line.strip()) for line in f.readlines()]

if __name__ == "__main__":
    main()
