def findLongestConseqSubseq(arr, n):
    ans = 0
    count = 0

    arr.sort()

    v = [arr[0]]
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            v.append(arr[i])

    for i in range(len(v)):
        if i > 0 and v[i] == v[i - 1] + 1:
            count += 1
        else:
            count = 1
        ans = max(ans, count)
    return ans


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    print(findLongestConseqSubseq(arr, n))


if __name__ == '__main__':
    main()