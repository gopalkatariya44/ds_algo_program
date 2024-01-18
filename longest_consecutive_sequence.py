import sys


def consecutive_sequence_ap1(nums):
    sorted_nums = sorted(nums)

    last_small = -sys.maxsize
    long, count = 1, 0
    for i in range(len(sorted_nums)):
        if sorted_nums[i] - 1 == last_small:
            count += 1
            last_small = sorted_nums[i]

        elif sorted_nums[i] != last_small:
            count = 1
            last_small = sorted_nums[i]
        if count > long:
            long = count

    return long


def consecutive_sequence_ap2(nums):
    if len(nums) == 0: return 0
    nums_set = set(nums)
    longest = 1
    for i in nums_set:
        if i - 1 not in nums_set:
            cnt = 1
            x = i
            while x + 1 in nums_set:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest


if __name__ == '__main__':
    nums = [100, 100, 103, 104, 102, 4, 3, 2, 1, 3, 1, 1, 1, 2, 5]
    # print(consecutive_sequence_ap1(nums))
    print("=", consecutive_sequence_ap2(nums))
