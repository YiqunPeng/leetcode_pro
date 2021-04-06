class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        p = 0
        v = 0
        cnt = 0
        bp = None
        while p < len(s):
            if not bp:
                if '0' <= s[p] <= '9':
                    v = v * 10 + int(s[p])
                elif s[p] == '[':
                    bp = p
                    cnt += 1
                else:          
                    res.append(s[p])
            else:
                if s[p] == '[':
                    cnt += 1               
                elif s[p] == ']':
                    cnt -= 1
                    if cnt == 0:
                        res.append(self.decodeString(s[bp+1:p]) * v)
                        v = 0
                        bp = None
            p += 1
        return ''.join(res)
