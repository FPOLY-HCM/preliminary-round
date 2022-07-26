def main():
    m = int(input())
    for i in range(m, 0, -1):
        for j in range(m - i):
            print(' ', end='')

        for j in range(2 * i - 1):
            print("*", end='')

        print()


if __name__ == '__main__':
    main()
