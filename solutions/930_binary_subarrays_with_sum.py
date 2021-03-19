class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """Presum array.
        """
        d = collections.defaultdict(int)
        d[0] = 1
        pres = 0
        res = 0
        for a in A:
            pres += a
            res += d[pres - S]
            d[pres] += 1
        return res
