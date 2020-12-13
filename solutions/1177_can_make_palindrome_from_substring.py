class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """String.

        Running time: O(n + m) where n == len(s) and m == len(queries).
        """
        n = len(s)
        arr = [[0] * (n + 1) for i in range(26)]
        ord_a = ord('a')
        for i in range(n):
            for j in range(26):
                if j == ord(s[i]) - ord_a:
                    arr[j][i+1] = arr[j][i] + 1
                else:
                    arr[j][i+1] = arr[j][i]
        res = []
        for l, r, k in queries:
            c = 0
            for j in range(26):
                if (arr[j][r+1] - arr[j][l]) % 2 == 1:
                    c += 1
            if c // 2 <= k:
                res.append(True)
            else:
                res.append(False)
        return res
