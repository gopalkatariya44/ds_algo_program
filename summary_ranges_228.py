class Solution:
    def add_ans(self, num1, num2):
        if num1 != num2:
            return f"{num1}->{num2}"
        else:
            return str(num1)

    def summary_ranges(self, nums):
        count = 0
        if len(nums) == 0: return []
        i, j = 0, 0
        ans = []
        while j < (len(nums) - 1):
            count += 1
            if nums[j] + 1 == nums[j + 1]:
                j += 1
            else:
                ans.append(self.add_ans(nums[i], nums[j]))
                j += 1
                i = j

        ans.append(self.add_ans(nums[i], nums[j]))
        print(count)
        return ans


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    nums = []
    nums = [0, 2, 3, 4, 6, 8, 9]
    solution = Solution()

    print(solution.summary_ranges(nums))
