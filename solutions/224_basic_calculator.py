class Solution:
    def calculate(self, s: str) -> int:
        """Stack.
        """
        val = 0
        num = 0
        sign = 1
        st = []
        for c in s:
            if '0' <= c <= '9':
                num = num * 10 + int(c)
            elif c == '-':
                val += sign * num
                num = 0
                sign = -1
            elif c == '+':
                val += sign * num
                num = 0
                sign = 1
            elif c == '(':
                st.append(val)
                st.append(sign)
                val = 0
                sign = 1
            elif c == ')':
                val += sign * num
                val *= st.pop()
                val += st.pop()
                num = 0
                sign = 1
        return val + sign * num
