def merge_sorted_arrays_ap1(nums1, nums2):
    n1, n2 = 0, 0
    ans = []
    while n1 < len(nums1) and n2 < len(nums2):
        if nums1[n1] <= nums2[n2]:
            ans.append(nums1[n1])
            n1 += 1
        else:
            ans.append(nums2[n2])
            n2 += 1
    while n1 < len(nums1):
        ans.append(nums1[n1])
        n1 += 1
    while n2 < len(nums2):
        ans.append(nums2[n2])
        n2 += 1
    for i in range(len(nums1) + len(nums2) - 1):
        if i < len(nums1):
            nums1[i] = ans[i]
        else:
            nums2[i - len(nums1)] = ans[i]
    print(ans)
    print(nums1, nums2)


def merge_sorted_arrays_ap2(nums1, nums2):
    n1, n2 = len(nums1) - 1, 0

    while n1 >= 0 and n2 < len(nums2):
        print(nums1[n1], nums2[n2])
        if nums1[n1] > nums2[n2]:
            nums1[n1], nums2[n2] = nums2[n2], nums1[n1]
            n1 -= 1
            n2 += 1
        else:
            break
    nums1, nums2 = sorted(nums1), sorted(nums2)
    print(nums1, nums2)


if __name__ == '__main__':
    nums1, nums2 = [1, 3, 5, 7], [0, 2, 6, 8, 9]
    merge_sorted_arrays_ap2(nums1, nums2)
