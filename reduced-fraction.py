def uscln(a, b):
    if b == 0:
        return a

    return uscln(b, a % b)


def main():
    strinput = input()
    alo = strinput.split()
    a = int(alo[0])
    b = int(alo[1])

    uln = uscln(a, b)

    outa = int(a / uln)
    outb = int(b / uln)

    if outb == 1:
        print(str(outa))
    else:
        print(str(outa) + ' ' + str(outb))


if __name__ == '__main__':
    main()
