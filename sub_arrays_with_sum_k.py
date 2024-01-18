def sub_array_ap1(nums, k):
    ans = []
    for i in range(len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            if sum(nums[i:j]) == k:
                ans.append(nums[i: j])
    return len(ans), ans


def sub_array_ap2(nums, k):
    ans = []
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            print(nums[j])
            total += nums[j]
            if total == k:
                ans.append(nums[i: j + 1])
    return len(ans), ans


def sub_array_ap3(nums, k):
    count = 0
    pre_sum = 0
    d = {0: 1}

    for i in nums:
        pre_sum += i
        remove = pre_sum - k
        if remove not in d.keys(): d[remove] = 0
        count += d[remove]
        if pre_sum not in d.keys():
            d[pre_sum] = 1
        else:
            d[pre_sum] += 1
    print(d)
    return count


if __name__ == '__main__':
    nums = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    print(sub_array_ap3(nums, 3))
