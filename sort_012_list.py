def sort_012_list_ap1(lst):
    zero = 0
    one = 0
    two = 0

    for i in lst:
        if i == zero:
            zero += 1
        elif i == one:
            one += 1
        else:
            two += 1

    temp = []
    for i in range(zero): temp.append(0)
    for i in range(one): temp.append(1)
    for i in range(two): temp.append(2)

    return temp


def sort_012_list_ap2(lst):
    low, mid, high = 0, 0, (len(lst) - 1)

    while mid <= high:
        print(lst)
        print(low, mid, high)
        if lst[mid] == 0:
            lst[mid], lst[low] = lst[low], lst[mid]
            low += 1
            mid += 1
        elif lst[mid] == 1:
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[high] = lst[high], lst[mid]
            high -= 1

    return lst


if __name__ == '__main__':
    lst = [0, 0, 1, 2, 0, 0, 2, 2, 2, 1, 1, 2, 2, 0]
    lst1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]
    print(sort_012_list_ap2(lst1))
