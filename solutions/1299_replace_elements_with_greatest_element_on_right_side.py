class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of arr.
    	"""
        max_v = arr[-1]
        arr[-1] = -1
        
        for i in range(len(arr) - 2, -1, -1):
            t = arr[i]
            arr[i] = max_v
            max_v = max(max_v, t)
            
        return arr