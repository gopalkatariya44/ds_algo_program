def missing(a: list, n: int):
    xor1, xor2 = 0, 0

    for i in range(n - 1):
        xor1 = xor1 ^ (i + 1)
        xor2 = xor2 ^ a[i]

    xor1 = xor1 ^ n

    return xor1 ^ xor2


def missing1(a: list, n: int):
    to = n * (n + 1) / 2
    return to - sum(a)


def missing2(a: list, n: int):
    h = [0] * (n+1)
    for i in a:
        h[i] = 1

    print(h)
    for i in range(1, len(h)):
        if h[i] == 0:
            return i


def missing3(a: list, n: int):
    for i in range(1, n):
        flag = 0
        for j in a:
            if j == i:
                flag = 1
                break
        if flag == 0:
            return i


if __name__ == '__main__':
    ls = [1, 2, 4, 5, 3, 7]
    print(missing2(ls, 7))
