class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        """String.
        """
        srl = self._run_length(S)
        res = 0
        for word in words:
            wrl = self._run_length(word)
            if len(srl) == len(wrl):
                for i in range(len(srl)):
                    if srl[i][0] != wrl[i][0] or srl[i][1] < wrl[i][1]:
                        break
                    if srl[i][1] < 3 and srl[i][1] != wrl[i][1]:
                        break
                else:
                    res += 1
        return res
        
    def _run_length(self, s):
        if not s:
            return []
        r = []
        c = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                r.append([s[i-1], c])
                c = 1
            else:
                c += 1
        return r + [[s[-1], c]]
