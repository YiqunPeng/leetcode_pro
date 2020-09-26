class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """Sliding window.

        Running time: O(n) where n is the length of data.
        """
        c = sum(data)
        z = 0
        s = sum(data[:c])
        res = c - s
        for i in range(c, len(data)):
            if data[i-c] == 1:
                s -= 1
            if data[i] == 1:
                s += 1
            res = min(res, c - s)
        return res
