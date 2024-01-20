class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = count1
                count1 += 1
            if t[i] not in td:
                td[t[i]] = count2
                count2 += 1
        sl = []
        tl = []
        for i, j in zip(s, t):
            sl.append(sd[i])
            tl.append(td[j])
        print(sl)
        print(tl)
        return sl == tl

    def isIsomorphic1(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        print(map1)
        print(map2)
        if map1 == map2:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = 'paper'
    t = 'title'
    print(solution.isIsomorphic1(s, t))
