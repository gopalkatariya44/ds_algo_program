def bubble_sort(nums):
    for i in range(len(nums)):
        print(nums)
        for j in range(1, len(nums)-i):
            if nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [3, 0, 1, 5, 7, 45, 6, 10, 9]
    nums = [3, 1, 12, 11, 100, 90, 2, 0]
    print(bubble_sort(nums))
