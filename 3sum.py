import time


def sum_of_3_ap1(nums):
    start = time.time()
    ans_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    if sorted([nums[i], nums[j], nums[k]]) not in ans_list:
                        ans_list.append(sorted([nums[i], nums[j], nums[k]]))
    print(time.time() - start)
    return ans_list


def sum_of_3_ap2(nums):
    start = time.time()
    ans_list = []
    for i in range(len(nums)):
        has_set = set()
        for j in range(i + 1, len(nums)):
            third = -(nums[i] + nums[j])
            temp = sorted([nums[i], nums[j], third])
            if third in has_set and temp not in ans_list:
                ans_list.append(temp)
            has_set.add(nums[j])
            # print(has_set)

    print(time.time() - start)
    return ans_list


def sum_of_3_ap3(nums):
    start = time.time()
    nums = sorted(nums)
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]: continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            temp = [nums[i], nums[j], nums[k]]
            if sum(temp) < 0:
                j += 1
            elif sum(temp) > 0:
                k -= 1
            else:
                if temp not in ans:
                    ans.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    print(time.time() - start)
    return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [41204, 6323, 5021, 27767, -18684, 89279, 16935, -10093, -9753, -5202, 83041, 9491, 35206, -3786, 25148]
    nums = [-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]
    print(sum_of_3_ap1(nums))
    print(sum_of_3_ap2(nums))
    print(sum_of_3_ap3(nums))
