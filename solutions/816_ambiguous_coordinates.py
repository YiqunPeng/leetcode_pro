class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        """String.
        """
        res = []
        for i in range(2, len(S) - 1):
            l = self._add_decimal_point(S[1:i])
            r = self._add_decimal_point(S[i:-1])
            for ll in l:
                for rr in r:
                    res.append(str('(') + ll + str(', ') + rr + str(')'))
        return res
    
    def _add_decimal_point(self, s):
        if self._is_valid_int(s):
            r = [s]
        else:
            r = []
        for i in range(1, len(s)):
            if self._is_valid_int(s[:i]) and self._is_valid_decimal(s[i:]):
                r.append(s[:i] + '.' + s[i:])
        return r
    
    def _is_valid_int(self, n):
        if n[0] == '0':
            return len(n) == 1
        else:
            return True
        
    def _is_valid_decimal(self, n):
        return n[-1] != '0'
