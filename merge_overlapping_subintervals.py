def merge_overlapping_subintervals_ap1(nums):
    nums = sorted(nums)
    ans = []
    for i in range(len(nums)):
        start = nums[i][0]
        end = nums[i][1]
        if ans and end <= ans[-1][1]:
            continue
        for j in range(i + 1, len(nums)):
            if nums[j][0] <= end:
                end = max(end, nums[j][1])
            else:
                break
        ans.append([start, end])
    return ans


def merge_overlapping_subintervals_ap2(nums):
    nums = sorted(nums)
    ans = []

    for i in range(len(nums)):
        if not ans or ans[-1][1] < nums[i][0]:
            ans.append(nums[i])
        else:
            ans[-1][1] = max(ans[-1][1], nums[i][1])
    return ans


if __name__ == '__main__':
    nums = [[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]
    print(merge_overlapping_subintervals_ap1(nums))
    print(merge_overlapping_subintervals_ap2(nums))
