def zero_to_end(lst):
    j = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            j = i
            break
    for i in range(j+1, len(lst)):
        if lst[i] != 0:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    print(lst)


if __name__ == '__main__':
    zero_to_end([1, 4, 1, 0, 0, 1, 3, 4, 10, 0, 5, 3, 0, 1, 2, 0])
    zero_to_end([2, 1])
