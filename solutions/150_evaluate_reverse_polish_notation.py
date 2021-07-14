class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Stack.
        """
        st = []
        for t in tokens:
            if t == '+':
                a, b = st.pop(), st.pop()
                st.append(b + a)
            elif t == '-':
                a, b = st.pop(), st.pop()
                st.append(b - a)
            elif t == '*':
                a, b = st.pop(), st.pop()
                st.append(b * a)
            elif t == '/':
                a, b = st.pop(), st.pop()
                st.append(int(float(b) / a))
            else:
                st.append(int(t))
        return st[-1]
