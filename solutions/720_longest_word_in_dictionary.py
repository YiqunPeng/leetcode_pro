class Solution:
    def longestWord(self, words: List[str]) -> str:
        """Hash set.

        Running time: O(nlogn) where n is the length of words.
        """
        d = set([""])
        words.sort(key=len)
        for word in words:
            if word[:-1] in d:
                d.add(word)
        res = ""
        for i in d:
            if len(i) > len(res) or (len(i) == len(res) and i < res):
                res = i
        return res
        