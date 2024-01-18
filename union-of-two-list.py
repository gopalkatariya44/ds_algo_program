if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 8]
    b = [1, 5, 8, 10, 11]

    lst = []
    lst2 = []

    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if a[i] <= b[j]:
            if len(lst) == 0 or lst[-1] != a[i]:
                lst.append(a[i])
                # print(f"if->{len(lst)}->{lst[-1]}!={a[i]}->{lst[-1] != b[i]}")
            i += 1
        else:
            if len(lst) == 0 or lst[-1] != b[j]:
                lst.append(b[j])
                # print(f"el->{len(lst)}->{lst[-1]}!={a[j]}->{lst[-1] != b[j]}")
            j += 1
        print(lst)

    while n1 > i:
        if len(lst) == 0 or lst[-1] != a[i]:
            lst.append(a[i])
        i += 1

    while n2 > j:
        if len(lst) == 0 or lst[-1] != b[j]:
            lst.append(b[j])
        j += 1

    print(lst)
    print(list(zip(a, b)))

    for i in a + b:
        if i not in lst2:
            lst2.append(i)
    print(lst2)
    print(set(a+b))
