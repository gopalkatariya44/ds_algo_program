def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

        print(nums)


if __name__ == '__main__':
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    nums = [87, 23, 43, 23, 4, 123, 4, 123, 455, 678, 765432, 4, 5, 6, 54, 8, 43]
    nums = [3, 0, 1, 5, 7, 45, 6, 10, 9]

    insertion_sort(nums)
