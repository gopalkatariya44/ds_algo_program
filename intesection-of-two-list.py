def intersection_tow_list(a: list, b: list) -> list:
    lst = []

    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            lst.append(a[i])
            i += 1
            j += 1

    return lst


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 8]
    b = [1, 5, 8, 10, 11]
    ans = intersection_tow_list(a, b)
    print(ans)
    print(1 ^ 1 ^ 2 ^ 2 )
