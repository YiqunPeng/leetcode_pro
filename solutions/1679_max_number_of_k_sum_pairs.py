class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """Hash table.

        Running time: O(n) where n == len(nums).
        """
        c = Counter(nums)
        res = 0
        for key, v in c.items():
            if key * 2 == k:
                res += v // 2
            elif k - key in c:
                res += min(v, c[k-key])
                c[key] = 0
        return res
