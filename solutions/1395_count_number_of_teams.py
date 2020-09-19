class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """Array.

        Running time: O(n^2) where n is the length of rating.
        """
        res = 0
        n = len(rating)   
        for i in range(n):
            ll, lg, rl, rg = 0, 0, 0, 0
            for j in range(0, i):
                if rating[i] > rating[j]:
                    ll += 1
                if rating[i] < rating[j]:
                    lg += 1
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    rg += 1
                if rating[i] > rating[j]:
                    rl += 1
            res = res + ll * rg + rl * lg
        return res
