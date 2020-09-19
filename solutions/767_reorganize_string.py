class Solution:
    def reorganizeString(self, S: str) -> str:
        """Sort.

        Running time:O(nlogn) where n is the length of S.
        """
        if not S:
            return ''
        
        c = collections.Counter(S)
        l = sorted(list(c.items()), key=lambda x:x[1], reverse=True)
        
        p = 0
        rs = [''] * len(S)
        for i in range(len(l)):
            for j in range(l[i][1]):
                rs[p] = l[i][0]
                if 0 < p < len(S) - 1 and (rs[p-1] == rs[p] or rs[p] == rs[p+1]):
                    return ''
                p += 2
                if p >= len(S):
                    p = 1
        
        return ''.join(rs)