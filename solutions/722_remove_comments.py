class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        """String.

        Running time: O(k) where k is the total number of chars in source.
        """
        res = []
        buf = []
        in_b = False
        for line in source:
            i = 0
            while i < len(line):
                if in_b:
                    if line[i:i+2] == '*/':
                        in_b = False
                        i += 1
                else:
                    if line[i:i+2] == '/*':
                        in_b = True
                        i += 1
                    elif line[i:i+2] == '//':
                        break
                    else:
                        buf.append(line[i])
                i += 1
            if not in_b and buf:
                res.append(''.join(buf))
                buf = []
        return res
