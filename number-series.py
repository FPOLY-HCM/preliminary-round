def Factorial(number):
    num = 1
    for i in range(1, number + 1):
        num = num * i
    return num


def main():
    strinput = input().split()
    x = int(strinput[0])
    n = int(strinput[1])
    tong = 0

    for i in range(0, n + 1):
        tong += pow(x, n) / Factorial(i)
    print(tong)


if __name__ == '__main__':
    main()