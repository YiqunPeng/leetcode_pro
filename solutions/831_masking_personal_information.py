class Solution:
    def maskPII(self, S: str) -> str:
        """String.

        Running time: O(n) where n == len(S).
        """
        if '@' in S:
            return self._mask_email(S)
        else:
            return self._mask_phone_num(S)
        
    def _mask_email(self, s):
        splits = s.split('@')
        n = splits[0].lower()
        if len(n) == 1:
            return n + '*****' + n + '@' + splits[1].lower()
        else:
            return n[0] + '*****' + n[-1] + '@' + splits[1].lower()
        
    def _mask_phone_num(self, s):
        c = 0
        l_4 = ''
        for i in range(len(s) - 1, -1, -1):
            if s[i] in string.digits:
                c += 1
                if c <= 4:
                    l_4 = s[i] + l_4
        if c == 10:
            return '***-***-' + l_4
        else:
            return '+' + '*' * (c - 10) + '-***-***-' + l_4
