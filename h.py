def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while n > 0:
        if nums1[m - 1] >= nums2[n - 1] and m > 0:
            nums1[m + n - 1] = nums1[m - 1]
            print(m)
            m -= 1
            print(f'1if={nums1}')
        else:
            nums1[m + n - 1] = nums2[n - 1]
            print(n)
            n -= 1
            print(f'1el={nums1}')


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    merge(nums1, 3, nums2, 3)
    print(nums1)
