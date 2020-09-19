class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """String.

        Running time: O(p) where p is the length of paragraph.
        """
        words = []
        word = ''
        for c in paragraph:
            if c.isalpha():
                word += c.lower()
            elif not c.isalpha() and word:
                words.append(word)
                word = ''
        if word:
            words.append(word)
        
        banned = set(banned)
        
        fre = collections.defaultdict(int)
        for word in words:
            if word not in banned:
                fre[word] += 1
        
        res, f = '', 0
        for k, v in fre.items():
            if v > f:
                res, f = k, v
        return res