class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        while s and g:
            if g[-1] <= s[-1]:
                res += 1
                g.pop()
                s.pop()
            elif s:
                s.pop()
        return res