class Solution:
    def calculate(self, s: str) -> int:
        """Recursion.
        """
        q = deque()
        for c in s:
            q.append(c)
        q.append('+')
        return self._recursion(q)
    
    def _recursion(self, q):
        res = 0
        num = 0
        temp = 0
        sign = '+'
        while q:
            c = q.popleft()
            if '0' <= c <= '9':
                num = num * 10 + int(c)
            elif c == '(':
                num = self._recursion(q)
            elif c in '+-*/)':
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
                if c == ')':
                    break
                num = 0
                sign = c
        return res + temp
