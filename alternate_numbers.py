def alternate_numbers(arr):
    neg, pos = [], []

    for el in arr:
        if el > 0:
            pos.append(el)
        else:
            neg.append(el)

    if len(pos) > len(neg):
        for i in range(len(neg)):
            print(2 * i, 2 * i + 1)
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            print(2 * i, 2 * i + 1)
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1


if __name__ == '__main__':
    arr = [1, 2, -4, -5, 2, -3, -2]
    alternate_numbers(arr)
    print(arr)
