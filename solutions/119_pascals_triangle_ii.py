class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	"""Math.

    	Running time: O(rowIndex)
    	"""
        ret = [0] * (rowIndex + 1)
        ret[0] = 1
        
        for c in range(1, rowIndex + 1):
            ret[c] = ret[c-1] * (rowIndex + 1 - c) // c
            
        return ret
