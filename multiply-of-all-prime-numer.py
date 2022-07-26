def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def main():
    str = input()
    alo = str.split()
    m = int(alo[0])
    n = int(alo[1])
    tong = 1

    if m < 2 and n < 2:
        tong = 1
        print(tong)
        return

    if m < 2:
        m = 2

    if n < 2:
        n = 2

    if m > n:
        for i in range(n, m + 1):
            if is_prime(i):
                tong *= i
    elif m <= n:
        for i in range(m, n + 1):
            if is_prime(i):
                tong *= i

    print(tong)


if __name__ == '__main__':
    main()