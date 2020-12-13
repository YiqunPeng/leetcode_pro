class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.

        Running time: O(n) where n == len(strs).
        """
        res = []
        for s in strs:
            res += [str(len(s)), '/', s]
        return ''.join(res)
        
        
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.

        Running time: O(n) where n == len(s).
        """
        res = []
        p = 0
        while p < len(s):
            t = p
            while s[p] != '/':
                p += 1
            v = int(s[t:p])
            res.append(s[p+1:p+1+v])
            p = p + 1 + v
        return res
