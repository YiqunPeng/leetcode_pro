class Solution:
    def calculate(self, s: str) -> int:
        """Stack.
        """
        res = 0
        num = 0
        temp = 0
        sign = '+'
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    res += temp
                    temp = num
                elif sign == '-':
                    res += temp
                    temp = -num
                elif sign == '*':
                    temp *= num
                elif sign == '/':
                    temp = int(float(temp) / num)
                sign = s[i]
                num = 0
        return temp + res
