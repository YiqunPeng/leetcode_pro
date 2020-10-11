class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int: 
    	"""Array.

    	Running time: O(n) where n is the length of arr.           
    	"""
        res = 0
        m = -1
        for i in range(len(arr)):
            m = max(m, arr[i])
            if m == i:
                res += 1
        return res
                           