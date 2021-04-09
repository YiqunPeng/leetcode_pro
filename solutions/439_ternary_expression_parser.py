class Solution:
    def parseTernary(self, expression: str) -> str:
        c, values = expression.split('?', 1)
        cnt = 0
        p = 0
        for i in range(len(values)):
            if values[i] == ':':
                if cnt > 0:
                    cnt -= 1
                else:
                    p = i
                    break
            elif values[i] == '?':
                cnt += 1
        tv, fv = values[:p] , values[p+1:]
        if c == 'T':
            if tv.find('?') == -1:
                return tv
            else:
                return self.parseTernary(tv)
        else:
            if fv.find('?') == -1:
                return fv
            else:
                return self.parseTernary(fv)
