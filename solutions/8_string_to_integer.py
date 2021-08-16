class Solution:
    def myAtoi(self, s: str) -> int:
        max_value = 2 ** 31 - 1
        min_value = -2 ** 31
        num = 0
        digit_only = False
        sign = None
        for c in s:
            if '0' <= c <= '9':
                digit_only = True
                c = int(c)
                if num is None:
                    num = 0
                if sign == '-':
                    if (num == 214748364 and c > 8) or (num > 214748364):
                        return min_value
                else:
                    if (num == 214748364 and c > 7) or (num > 214748364):
                        return max_value
                num = num * 10 + c
            else:
                if digit_only:
                    return -num if sign == '-' else num
                if c == ' ':
                    continue
                if c in '+-':
                    digit_only = True
                    if sign is not None:
                        return -num if sign == '-' else num
                    sign = c
                else:
                    return -num if sign == '-' else num
        return -num if sign == '-' else num
