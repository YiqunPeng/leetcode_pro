class Solution:
    def longestWord(self, words: List[str]) -> str:
        """Hash set.

        Running time: O(nlogn) where n is the length of words.
        """
        words.sort(key=lambda x:len(x))
        
        res = set([])
        
        for word in words:
            if len(word) == 1 or word[:-1] in res:
                res.add(word)
        
        if res:
            return sorted(list(res), key=lambda x:(-len(x), x))[0]
        else:
            return ''
        