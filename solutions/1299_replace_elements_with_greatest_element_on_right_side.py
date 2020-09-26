class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of arr.
    	"""
        n = len(arr)
        res = [0] * (n - 1) + [-1] 
        m = arr[-1]
        for i in range(n - 2, -1, -1):
            res[i] = m
            m = max(m, arr[i])
        return res
