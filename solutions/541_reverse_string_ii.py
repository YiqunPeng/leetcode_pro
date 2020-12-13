class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        li = list(s)
        p = 0
        for i in range(0, len(s), 2 * k):
            l, r = i, min(i + k - 1, len(li) - 1)
            while l < r:
                li[l], li[r] = li[r], li[l]
                l += 1
                r -= 1
        return ''.join(li)
