class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """Hash table.

        Running time: O(n) where n is the length of words.
        """
        def get_dict(word):
            d = collections.defaultdict(int)
            for c in word:
                if c.lower() in string.ascii_lowercase:
                    d[c.lower()] += 1
            return d
        
        plate = get_dict(licensePlate)
        res = None
        
        for word in words:
            d = get_dict(word)
            for k, v in plate.items():
                if k not in d or d[k] < v:
                    break
            else:
                if not res or len(res) > len(word):
                    res = word
        
        return res
