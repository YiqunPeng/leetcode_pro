class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """String.

        Running time: O(n^2) where n == len(strs).
        """
        strs.sort(key=len, reverse=True)
        n = len(strs)
        for i in range(n):
            for j in range(n):
                if i != j and self._is_subseq(strs[i], strs[j]):
                    break
            else:
                return len(strs[i])
        return -1
    
    def _is_subseq(self, si, sj):
        i = 0
        for c in sj:
            if i < len(si) and si[i] == c:
                i += 1
        return i == len(si)
