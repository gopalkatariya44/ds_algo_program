def rearrange_array(nums):
    ans = [0] * len(nums)
    i, j = 0, 1
    for num in nums:
        if num > 0:
            ans[i] = num
            i += 2
        else:
            ans[j] = num
            j += 2
    print(ans)





if __name__ == '__main__':
    nums = [3, 1, -2, -5, 2, -4]
    rearrange_array(nums)
