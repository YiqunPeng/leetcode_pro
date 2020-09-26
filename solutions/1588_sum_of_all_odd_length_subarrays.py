class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """Array.

        Running time: O(n^2) where n is the length of arr.
        """
        n = len(arr)
        res = 0
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + arr[i-1]
        for l in range(1, n + 1, 2):
            for i in range(0, n - l + 1):
                res += prefix[i+l] - prefix[i]
        return res