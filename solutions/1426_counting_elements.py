class Solution:
    def countElements(self, arr: List[int]) -> int:
    	"""Hash table.

    	Running time: O(n) where n is the length of arr.
    	"""
        c = collections.Counter(arr)
        res = 0
        for k, v in c.items():
            if k + 1 in c:
                res += v
        return res
