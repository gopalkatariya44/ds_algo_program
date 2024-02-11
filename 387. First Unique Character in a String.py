class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:i]:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar('leetcode'))
    print(s.firstUniqChar('loveleetcode'))
    print(s.firstUniqChar('aabb'))