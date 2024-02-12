class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(n):
            ans.append([0] * n)
        top, left, right, bottom = 0, 0, n - 1, n - 1

        count = 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans[top][i] = count
                count += 1
            top += 1
            for i in range(top, bottom + 1):
                ans[i][right] = count
                count += 1
            right -= 1
            for i in range(right, left, -1):
                ans[bottom][i] = count
                count += 1
            bottom -= 1
            for i in range(bottom + 1, top - 1, -1):
                ans[i][left] = count
                count += 1
            left += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 9
    mat = s.generateMatrix(9)
    for i in mat:
        print(i)
