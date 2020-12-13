class Solution:
    def maxRepOpt1(self, text: str) -> int:
        """String.

        Running time: O(n) where n == len(text).
        """
        c = 1
        l = []
        f = {text[0]: 1}
        for i in range(1, len(text)):
            if text[i] == text[i-1]:
                c += 1
            else:
                l.append([text[i-1], c])
                c = 1
            f[text[i]] = f.get(text[i], 0) + 1
        l.append([text[-1], c])
        res = 0
        for i in range(len(l)):
            if l[i][1] == f[l[i][0]]:
                res = max(res, l[i][1])
            else:
                res = max(res, l[i][1] + 1)
            if i + 2 < len(l) and l[i+1][1] == 1 and l[i][0] == l[i+2][0]:
                if l[i][1] + l[i+2][1] == f[l[i][0]]:
                    res = max(res, f[l[i][0]])
                else:
                    res = max(res, l[i][1] + l[i+2][1] + 1)
        return res
