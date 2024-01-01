class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        length = len(s)
        count = 0
        for i in range(length):
            if g[count] <= s[i]:
                count += 1
            if count == len(g):
                break
        return count
