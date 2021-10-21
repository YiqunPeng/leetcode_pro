class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        j = (tomatoSlices - 2 * cheeseSlices) / 2.0
        if 0 <= j <= cheeseSlices and j == int(j):
            return [int(j), cheeseSlices - int(j)]
        else:
            return []
