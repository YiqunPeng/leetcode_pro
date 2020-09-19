class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int: 
    	"""Array.

    	Running time: O(n) where n is the length of arr.           
    	"""
        res = 0     
        p, r = 0, 0 
        
        while p < len(arr):
            r = max(r, arr[p])    
            if r == p:
                res += 1
            p += 1
        
        return res
                           