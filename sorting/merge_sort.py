def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    print("r-left-> ", nums[:mid], "r-right-> ", nums[mid:])

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    print("left-> ", left, "right-> ", right)

    i, j = 0, 0
    ans = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    while i < len(left):
        ans.append(left[i])
        i += 1
    while j < len(right):
        ans.append(right[j])
        j += 1
    print("ans-> ", ans)
    return ans


if __name__ == '__main__':
    nums = [2, 3456, 543, 345, 43, 3456, 433, 454, 1, 0]
    nums = [100, 9, 8, 7, 6, 1, 4, 2, 3, 5]
    print(merge_sort(nums))
