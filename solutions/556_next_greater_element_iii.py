class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """String.

        Running time: O(m) where m == len(str(n)).
        """
        m = str(2 ** 31 - 1)
        n = list(str(n))
        p = len(n) - 1
        while p > 0 and n[p] <= n[p-1]:
            p -= 1
        if p == 0:
            return -1
        q = len(n) - 1
        while q >= p and n[q] <= n[p-1]:
            q -= 1
        n[p-1], n[q] = n[q], n[p-1]
        res = ''.join(n[:p] + n[p:][::-1])
        if len(res) > len(m) or (len(res) == len(m) and m < res):
            return -1
        else:
            return int(res)
