class Solution:
    def minDeletions(self, s: str) -> int:
        """Sorting.

        Running time: O(nlogn) where n == len(s).
        """
        counter = Counter(s)
        res = 0
        values = sorted(counter.values(), reverse=True)
        for i in range(1, len(values)):
            expected = max(0, values[i-1] - 1)
            diff = max(0, values[i] - expected)
            values[i] -= diff
            res += diff
        return res
