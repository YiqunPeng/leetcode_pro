class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
    	"""Hash table.

    	Running time: O(k) where n is the total number of characters of all words.
    	"""
        from collections import Counter
        
        c = Counter(chars)
        ret = 0
        
        for word in words:
            w = Counter(word)
            if all(c[k] >= w[k] for k in w):
                ret += len(word)
        
        return ret