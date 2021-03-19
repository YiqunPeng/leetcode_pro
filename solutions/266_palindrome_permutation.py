class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
    	"""Hash table.

    	Running time: O(n) where n == len(s).
    	"""
        c = collections.Counter(s)
        return sum([1 for i in c.values() if i % 2]) - len(s) % 2 == 0
