class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(arr).
        """
        o, e = 0, 0
        res = 0
        mod = 10 ** 9 + 7
        for a in arr:
            if a % 2 == 0:
                o, e = o, e + 1
                res = (res + o) % mod
            else:
                o, e = e + 1, o
                res = (res + o) % mod 
        return res
