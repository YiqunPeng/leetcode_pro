class Solution:
    def numSub(self, s: str) -> int:
        """String.
            
        Running time: O(n) where n == len(s).
        """
        c = 0
        res = 0
        mod = 10 ** 9 + 7
        for i in s:
            if i == '0':
                res = (res + (c + 1) * c // 2 % mod) % mod
                c = 0
            else:
                c += 1
        return (res + (c + 1) * c // 2 % mod) % mod
