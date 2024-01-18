def max_sum_ap1(nums):
    max_sum = -1010101
    for i in range(len(nums)):
        sub_arr = []
        for j in range(i, len(nums)):
            sub_arr.append(nums[j])
            max_sum = max(max_sum, sum(sub_arr))

    return max_sum


def max_sum_ap2(nums):
    sm, mx = 0, -345453456546456

    for i in range(len(nums)):
        sm += nums[i]
        if sm < 0:
            sm = 0
        if sm > mx:
            mx = sm

    return mx


if __name__ == '__main__':
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    nums1 = [12, -3, 4, -1, -20, 1, 15, -3]
    nums2 = [-1, -2, 3, -4, 5, 6, -10, 20]
    nums3 = [-4, -3, -2, -1]
    print(max_sum_ap2(nums3))
