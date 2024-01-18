def count_subarray_ap1(nums, k):
    ans = []
    for i in range(len(nums)):
        temp = []
        for j in range(i, len(nums)):
            temp.append(nums[j])
            sum = 0
            for t in temp:
                sum ^= t
            if sum == k:
                ans.append(temp.copy())
    return ans


def count_subarray_ap2(nums, k):
    xr = 0
    mp = {}
    mp[0] = 1
    count = 0
    for i in range(len(nums)):
        xr ^= nums[i]
        x = xr ^ k
        if x in mp:
            count += mp[x]
        if xr in mp:
            mp[xr] += 1
        else:
            mp[xr] = 1

    return count


if __name__ == '__main__':
    nums = [4, 2, 2, 6, 4]
    k = 6

    print(count_subarray_ap1(nums, k))
    print(count_subarray_ap2(nums, k))
