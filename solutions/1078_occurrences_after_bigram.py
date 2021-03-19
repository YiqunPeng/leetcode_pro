class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    	"""String.

    	Running time: O(n) where n is the number of words in text.
    	"""
        words = text.split(' ')
        res = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                res.append(words[i+2])
        return res
