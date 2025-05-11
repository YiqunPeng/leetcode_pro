class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for w in words[1:]:       
            common &= Counter(w)
        res = []
        for k, v in common.items():
            res.extend([k] * v)
        return res