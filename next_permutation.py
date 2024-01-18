def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0:
        return [[]]
    result = []
    for i in range(len(nums)):
        for perm in permute(nums[:i] + nums[i + 1:]):
            result.append([nums[i]] + perm)
    return result


def next_permutation(nums):
    permutations = [int("".join([str(j) for j in i])) for i in permute(nums)]
    print(permutations)
    print("".join([f"{i}" for i in [1, 2, 3]]))


if __name__ == '__main__':
    nums = [1, 2, 3]
    next_permutation(nums)
# not completed

 