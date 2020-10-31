class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """Hash table.
        """
        n = len(rains)
        res = [1] * n
        f = {}
        s = []
        for i, r in enumerate(rains):
            if r > 0:
                if r in f:
                    idx = bisect.bisect_left(s, f[r])
                    if idx == len(s):
                        return []
                    else:    
                        res[s[idx]] = r
                        s.pop(idx)
                f[r] = i
                res[i] = -1
            else:
                s.append(i)
        return res  
