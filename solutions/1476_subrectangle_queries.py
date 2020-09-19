class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.r = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
    	"""Running time: O(n) where n is the number of item that needs update.
    	"""
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.r[i][j] = newValue
        
    def getValue(self, row: int, col: int) -> int:
    	"""Running time: O(1).
    	"""
        return self.r[row][col]


class SubrectangleQueries1:

    def __init__(self, rectangle: List[List[int]]):
        self.r = rectangle
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
    	"""Running time: O(1).
    	"""
        self.updates.append((row1, col1, row2, col2, newValue))
        
    def getValue(self, row: int, col: int) -> int:
    	"""Running time: O(k) where k is the length of self.updates.
    	"""
        for r1, c1, r2, c2, v in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return v
        return self.r[row][col]