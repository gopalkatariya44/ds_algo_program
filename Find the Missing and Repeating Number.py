def ap1(nums, n):
    missing = -1
    repeating = -1
    for i in range(1, len(nums)):
        count = 0
        for j in nums:
            if j == i:
                count += 1
        if count == 2:
            repeating = i
        elif count == 0:
            missing = i
        if missing != -1 and repeating != -1:
            break

    return repeating, missing


def ap2(nums, n):
    hash_arr = [0] * (n + 1)
    for i in nums:
        hash_arr[i] = hash_arr[i] + 1

    return hash_arr[1:].index(2) + 1, hash_arr[1:].index(0) + 1


def ap3(nums, n):
    sn = (n * (n + 1)) / 2
    s2n = (n * (n + 1)) * (2 * n + 1) / 6
    s, s2 = 0, 0
    for i in range(len(nums)):
        s += nums[i]
        s2 += (nums[i] * nums[i])

    val1 = s - sn
    val2 = s2 - s2n

    val2 = val2 / val1
    x = (val1 + val2) / 2
    y = x - val1

    return int(x), int(y)


def ap4(nums, n):
    pass


if __name__ == '__main__':
    nums, n = [4, 3, 6, 2, 1, 1], 6
    print(ap1(nums, n))
    print(ap2(nums, n))
    print(ap3(nums, n))
