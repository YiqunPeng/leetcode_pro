class Solution:
    def calculate(self, s: str) -> int:
        """Stack.
        """
        return self._calc(s, 0)
    
    def _calc(self, s, idx):
        num = 0
        sign = '+'
        st = []
        while idx < len(s):
            c = s[idx]
            if '0' <= c <= '9':
                num = num * 10 + int(c)
            elif c in '+-*/':
                self._update_stack(st, sign, num)
                num = 0
                sign = c
            idx += 1
        self._update_stack(st, sign, num)
        return sum(st)                
                
    def _update_stack(self, st, sign, num):
        if sign == '+':
            st.append(num)
        if sign == '-':
            st.append(-num)
        if sign == '*':
            st.append(st.pop() * num)
        if sign == '/':
            val = st.pop()
            if val * num < 0:
                st.append(-(abs(val) // abs(num)))
            else:
                st.append(val // num)
