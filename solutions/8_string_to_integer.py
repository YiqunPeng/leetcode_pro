class Solution:
    def myAtoi(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        p = 0
        while p < len(s) and s[p] == ' ':
            p += 1
        if p < len(s):
            if s[p] == '-':
                sign = '-'
                p += 1
            elif s[p] == '+':
                sign = '+'
                p += 1
            else:
                sign = '+'
        num = ''
        while p < len(s) and s[p] in string.digits:
            if num or s[p] != '0':
                num += s[p]
            p += 1
        if num:
            if self._is_int(num, sign):
                return int(num) if sign == '+' else -int(num)
            else:
                return -2147483648 if sign == '-' else 2147483647
        else:
            return 0
    
    def _is_int(self, num, sign):
        max_v, min_v = '2147483647', '2147483648'
        if len(num) > 10:
            return False
        elif len(num) < 10:
            return True
        else:
            return num < max_v if sign == '+' else num < min_v
