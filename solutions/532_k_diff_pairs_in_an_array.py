class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    	"""Hash table.

    	Running time: O(n) where n == len(nums).
    	"""
        c = Counter(nums)
        res = 0
        for key, v in c.items():
            if (k == 0 and v >= 2) or (k != 0 and key + k in c):
                res += 1
        return res
