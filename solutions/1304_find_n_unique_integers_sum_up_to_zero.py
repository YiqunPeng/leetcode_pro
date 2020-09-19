class Solution:
    def sumZero(self, n: int) -> List[int]:
    	"""Array.

    	Running time: O(n).
    	"""
        if n % 2 == 0:
            return [i for i in range(n // 2 * 2 - 1, - n // 2 * 2, -2)]
        else:
            return [i for i in range(n // 2, - n // 2, -1)]
