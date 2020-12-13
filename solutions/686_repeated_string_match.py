class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
    	"""String.

    	Running time: O(n * m) where n == len(a) and m == len(b).
    	"""
        mi = math.ceil(len(b) / len(a))
        for i in range(mi, mi + 2):
            if b in a * i:
                return i
        return -1
