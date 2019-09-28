class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """Hash table.

        Running time: O(N + t) where t is the length of trust.
        """
        c = set([i+1 for i in range(N)])
        g = [0] * (1 + N)

        for t in trust:
            g[t[1]] += 1
            c.discard(t[0])
        
        for i in c:
            if g[i] == N - 1:
                return i
        return -1