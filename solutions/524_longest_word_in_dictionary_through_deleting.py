class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        """String.

        Running time: O(kmn) where k is the number of strings in d, 
                      m is the length of string of in d, 
                      n is the length of s.
        """
        def is_subsequence(word):
            t = s
            for c in word:
                if c in t:
                    t = t[t.index(c)+1:]
                else:
                    return False
            return True
                
        
        d.sort(key=lambda x:(-len(x), x))
        for word in d:
            if is_subsequence(word):
                return word
        return ''
