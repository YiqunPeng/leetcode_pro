class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """Array.

        Running time: O(n * m) where m is the length of rounds.
        """
        f = [0] * n
        for i in range(len(rounds)-1):
            s, e = rounds[i], rounds[i+1]
            if e < s:
                e += n
            while s < e:
                f[s%n-1] += 1
                s += 1
        f[rounds[-1]-1] += 1
        m = max(f)
        res = []
        for i in range(n):
            if f[i] == m:
                res.append(i + 1)
        return res
