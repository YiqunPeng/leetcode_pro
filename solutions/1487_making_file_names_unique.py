class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        """Hash table.
        """
        res = []
        d = {}
        for n in names:
            if n not in d:
                d[n] = 1
                res.append(n)
            else:
                while n + '(' + str(d[n]) + ')' in d:
                    d[n] += 1
                res.append(n + '(' + str(d[n]) + ')')
                d[n + '(' + str(d[n]) + ')'] = 1
        return res
