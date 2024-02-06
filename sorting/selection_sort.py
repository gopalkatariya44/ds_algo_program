def selection_sort(nums):
    # Time O(n^2)
    # Space O(1)
    for i in range(len(nums) - 1):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j
        if min != i:
            nums[min], nums[i] = nums[i], nums[min]
    return nums


if __name__ == '__main__':
    nums = [3, 0, 1, 5, 7, 45, 6, 10, 9]
    an = selection_sort(nums)
    print(an)
