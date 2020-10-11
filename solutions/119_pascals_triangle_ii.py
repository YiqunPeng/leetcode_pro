class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	"""Math.

    	Running time: O(rowIndex^2).
    	"""
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j-1]
        return row
