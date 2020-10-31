class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        """String.

        Running time: O(n) where n is the length of A.
        """
        res = 0
        g = set()
        for a in A:
            p = self._get_group(a)
            if p not in g:
                g.add(p)
        return len(g)
    
    def _get_group(self, a):
        o, e = [0] * 26, [0] * 26
        orda = ord('a')
        for i in range(len(a)):
            if i % 2 == 0:
                e[ord(a[i]) - orda] += 1
            else:
                o[ord(a[i]) - orda] += 1
        return str([o, e])
