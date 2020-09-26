class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    	"""Array.

    	Running time: O(length + n), where n is the length of updates.
    	"""
        arr = [0] * length
        for s, e, i in updates:
            arr[s] += i
            if e + 1 < length:
                arr[e+1] -= i
        for i in range(1, length):
            arr[i] += arr[i - 1]
        return arr
