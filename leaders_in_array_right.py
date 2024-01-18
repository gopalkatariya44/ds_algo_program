import sys


def leaders_in_array_ap1(nums):
    leaders = []
    for i in range(len(nums)):
        flag = 0
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                flag = 1
                break
        if flag == 0:
            leaders.append(nums[i])
    return leaders


def leaders_in_array_ap2(nums):
    mx = -sys.maxsize
    leaders = []
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > mx:
            leaders.append(nums[i])
            mx = nums[i]
    return leaders


if __name__ == '__main__':
    nums = [10, 22, 12, 3, 0, 6]
    print(leaders_in_array_ap1(nums))
