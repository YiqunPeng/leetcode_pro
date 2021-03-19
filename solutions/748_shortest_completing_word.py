class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """Hash table.

        Running time: O(n) where n is the length of words.
        """
        words.sort(key=len)
        lc = {}
        for i in licensePlate:
            if i.lower().isalpha():
                lc[i.lower()] = lc.get(i.lower(), 0) + 1
        for word in words:
            wc = Counter(word)
            for k, v in lc.items():
                if k not in wc or wc[k] < v:
                    break
            else:
                return word
