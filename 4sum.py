def sum_of_4_ap1(nums, target):
    ans = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for l in range(k + 1, len(nums)):
                    temp = sorted([nums[i], nums[j], nums[k], nums[l]])
                    if sum(temp) == target and temp not in ans:
                        ans.append(temp)
    return ans


def sum_of_4_ap2(nums, target):
    ans = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            temp_arr = set()
            for k in range(j + 1, len(nums)):
                left = target - sum([nums[i], nums[j], nums[k]])
                if left in temp_arr:
                    temp = sorted([nums[i], nums[j], nums[k], left])
                    if temp not in ans:
                        ans.append(temp)

                temp_arr.add(nums[k])
    return ans


def sum_of_4_ap3(nums, target):
    nums = sorted(nums)
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]: continue
        for j in range(i+1, len(nums)):
            if j > i + 1 and nums[j - 1] == nums[j]: continue
            k = j + 1
            l = len(nums) - 1

            while k < l:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                s = sum(temp)
                if s < target:
                    k += 1
                elif s > target:
                    l -= 1
                else:
                    if temp not in ans:
                        ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k - 1] == nums[k]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return ans


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums = [1, 2, -1, -2, 2, 0, -1]
    nums = [1, 2, 3, 1, 3, 2, 1, 3, 2, 5, 4, 4, 4, 5]
    print(sum_of_4_ap1(nums, 8))
    print(sum_of_4_ap2(nums, 8))
    print(sum_of_4_ap3(nums, 8))
