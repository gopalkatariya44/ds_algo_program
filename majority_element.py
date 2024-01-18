def majority_element_ap1(lst):
    ele = 0
    count = 0
    for i in range(len(lst)):
        temp_count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                temp_count += 1
        if temp_count > count:
            count = temp_count
            ele = lst[i]
    return ele


def majority_element_ap2(lst):
    m = {}
    maj_ele = 0
    count = 0
    for i in range(len(lst)):
        if lst[i] not in m:
            m[lst[i]] = 1
        else:
            m[lst[i]] += 1
    for key, val in m.items():
        if val > count:
            count = val
            maj_ele = key
    print(m)
    return maj_ele


def majority_element_ap3(lst):
    count = 0
    ele = 0

    for i in range(len(lst)):
        if i == 0 or count == 0:
            count = 1
            ele = lst[i]
        elif ele == lst[i]:
            count += 1
        else:
            count -= 1
    count1 = 0
    for i in range(len(lst)):
        if lst[i] == ele:
            count1 += 1

    if count1 > len(lst) // 2:
        return ele
    return -1


if __name__ == '__main__':
    lst = [5, 5, 5, 5, 7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7]
    # lst = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    print(majority_element_ap3(lst))
