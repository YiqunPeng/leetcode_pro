class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
    	"""Hash set.

    	Running time: O(n) where n == len(s).
    	"""
        sub = set()
        for i in range(0, len(s) - k + 1):
            sub.add(s[i:i+k])
        return len(sub) == 2 ** k
