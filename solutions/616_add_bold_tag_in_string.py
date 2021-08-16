class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:        tag = [False] * len(s)
        tag = [False] * len(s)
        for w in words:
            i = s.find(w)
            while i != -1:
                for k in range(i, i + len(w)):
                    tag[k] = True
                i = s.find(w, i + 1)
        res = ''
        i = 0
        while i < len(s):
            if not tag[i]:
                res += s[i]
                i += 1
                continue
            res += '<b>'
            while i < len(s) and tag[i]:
                res += s[i]
                i += 1
            res += '</b>'
        return res
