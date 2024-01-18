def approach1(twice_num_list):
    for i in twice_num_list:
        count = 0
        for j in twice_num_list:
            if i == j:
                count += 1
        if count == 1:
            return i


def approach2(twice_num_list):
    hash_list = [0] * (twice_num_list[-1] + 1)
    for i in twice_num_list:
        hash_list[i] += 1
    print(hash_list)
    for i in range(1, len(hash_list)):
        if hash_list[i] == 1:
            return i


def approach3(twice_num_list):
    hash_dict = {}
    for i in twice_num_list:
        if i not in hash_dict:
            hash_dict[i] = 1
        else:
            hash_dict[i] += 1
    print(hash_dict)
    for i, j in hash_dict.items():
        if j == 1:
            return i


def approach4(twice_num_list):
    xor = 0
    for i in twice_num_list:
        xor ^= i
    return xor


if __name__ == '__main__':
    lst = [1, 1, 2, 2, 3, 3, 4, 4, 5, 8, 8]
    print(approach1(lst))
    print(approach2(lst))
    print(approach3(lst))
    print(approach4(lst))
