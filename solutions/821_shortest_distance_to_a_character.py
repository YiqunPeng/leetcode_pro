class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = []
        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)
        
        res = [0] * len(s)
        for i in range(0, pos[0]):
            res[i] = pos[0] - i
        for i in range(pos[-1]+1, len(res)):
            res[i] = i - pos[-1]
        
        for i in range(len(pos)-1):
            l, r = pos[i] + 1, pos[i+1] - 1
            v = 1
            while l <= r:
                res[l] = res[r] = v
                l, r, v = l + 1, r - 1, v + 1
        
        return res