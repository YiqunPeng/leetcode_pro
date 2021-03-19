class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """Hash table.

        Running time: O(n^2) where n == len(A).
        """
        s = collections.defaultdict(int)
        for a in A:
            for b in B:
                s[a+b] += 1
        res = 0
        for c in C:
            for d in D:
                if -c-d in s:
                    res += s[-c-d]
        return res
