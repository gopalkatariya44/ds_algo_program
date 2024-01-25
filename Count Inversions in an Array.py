def ap1(nums):
    ans = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                ans.append((nums[i], nums[j]))
    print(ans)
    return len(ans)


if __name__ == '__main__':
    nums = [5, 3, 2, 4, 1]
    print(ap1(nums))
