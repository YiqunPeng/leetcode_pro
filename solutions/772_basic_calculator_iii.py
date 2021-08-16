class Solution:
    def calculate(self, s: str) -> int:
        """Stack.
        """
        return self._calc(s, 0)[0]
    
    def _calc(self, s, idx):
        num = 0
        sign = '+'
        st = []
        while idx < len(s):
            c = s[idx]
            if '0' <= c <= '9':
                num = num * 10 + int(c)
            elif c == '(':
                num, n_idx = self._calc(s, idx + 1)
                idx = n_idx
            elif c == ')':
                self._update_stack(st, sign, num)
                return sum(st), idx
            else:
                self._update_stack(st, sign, num)
                sign = c
                num = 0
            idx += 1
        self._update_stack(st, sign, num)
        return sum(st), idx
    
    def _update_stack(self, st, sign, num):
        if sign == '+':
            st.append(num)
        if sign == '-':
            st.append(-num)
        if sign == '*':
            st.append(st.pop() * num)
        if sign == '/':
            v = st.pop()
            if v * num < 0:
                st.append(-(abs(v) // abs(num)))
            else:
                st.append(v // num)
