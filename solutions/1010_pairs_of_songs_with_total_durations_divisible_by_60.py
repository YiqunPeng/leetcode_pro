class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(time).
        """
        d = collections.defaultdict(int)
        for t in time:
            d[t % 60] += 1
        res = 0
        for k, v in d.items():
            if k == 0 or k == 30:
                res += (v - 1) * v // 2
            else:
                o = d.get(60 - k, 0)
                res += o * v / 2.0
        return int(res)
