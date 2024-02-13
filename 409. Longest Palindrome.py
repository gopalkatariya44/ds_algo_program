def longestPalindrome(s: str) -> int:
    if s == s[::-1]: return len(s)

    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    ls = list(d.values())
    l = 0
    ex = False
    for i in ls:
        if i == 1:
            ex = True
        elif i % 2 != 0:
            l += (i - 1) / 2
            ls.append(1)
        else:
            l += i / 2
    if ex:
        return 1 + int(l * 2)
    return int(l * 2)


if __name__ == '__main__':
    s = "awdfesgdhjhjngbfvdc"
    print(longestPalindrome(s))