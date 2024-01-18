def partition(lst, low, high):
    print(lst)
    pivot = lst[low]
    i = low
    j = high

    while i < j:
        while lst[i] <= pivot and i <= high - 1:
            i += 1
        while lst[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[low], lst[j] = lst[j], lst[low]
    return j


def qs(lst, low, high):
    if low < high:
        p_index = partition(lst, low, high)

        qs(lst, low, p_index - 1)
        qs(lst, p_index + 1, high)


if __name__ == '__main__':
    ls = [2, 0, 4, 6, 4, 7, 20, -1]
    qs(ls, 0, len(ls)-1)
    print(ls)



