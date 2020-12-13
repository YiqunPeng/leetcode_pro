class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """String.

        Running time: O(p) where p is the length of paragraph.
        """
        paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower()
        words = paragraph.split()
        banned = set(banned)        
        d = collections.defaultdict(int)
        res = None
        m = 0
        for w in words:
            if w in banned: 
                continue
            d[w] += 1
            if m < d[w]:
                m = d[w]
                res = w
        return res
