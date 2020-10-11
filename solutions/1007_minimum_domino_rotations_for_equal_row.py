class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """Array.

        Running time: O(a + b) where a is the length of A and b is the length of B.
        """
        n = len(A)
        c = collections.defaultdict(int)
        ca = collections.Counter(A)
        cb = collections.Counter(B)
        for i in range(n):
            if A[i] == B[i]:
                c[A[i]] += 1
            else:
                c[A[i]] += 1
                c[B[i]] += 1
        max_f, max_fv = max([(v, k) for k, v in c.items()]) 
        if max_f < n:
            return -1
        else:
            if len(c) == 2:
                return min([min(n - ca[k], n - cb[k]) for k in c.keys()])
            else:
                return min(n - ca[max_fv], n - cb[max_fv])
