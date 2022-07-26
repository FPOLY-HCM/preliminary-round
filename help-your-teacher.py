def main():
    n = int(input())
    names = []

    for i in range(n):
        names.append(input())

    sortName(names)

    for i in range(n):
        if i == n - 1:
            print(names[i], end='')
        else:
            print(names[i])


def sortName(names):
    names.sort(key=lambda x: x.split()[-1])

    return names


if __name__ == '__main__':
    main()



