class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    	"""String.

    	Running time: O(maxLetters*n) where n == len(s).
    	"""
        c = collections.Counter([s[i:i + minSize] for i in range(0, len(s) - minSize + 1)])
        return max([c[k] for k in c if len(set(k)) <= maxLetters] + [0])
