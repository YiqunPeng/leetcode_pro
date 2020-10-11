from functools import cmp_to_key

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """Sort.

        Running time: O(n * k + klogk) where n is the length of votes, and k is the number of teams. 
        """
        t = len(votes[0])
        pos = {}
        for rank in votes:
            for i in range(len(rank)):
                if rank[i] not in pos:
                    pos[rank[i]] = [0] * t + [rank[i]]
                pos[rank[i]][i] += 1
        return "".join([v[-1] for v in sorted(pos.values(), key=cmp_to_key(self._cmp))])
    
    def _cmp(self, a, b):
        for i in range(len(a) - 1):
            if a[i] != b[i]:
                return b[i] - a[i]
        return -1 if a[-1] < b[-1] else 1
