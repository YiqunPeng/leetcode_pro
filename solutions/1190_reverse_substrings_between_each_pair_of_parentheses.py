class Solution:
    def reverseParentheses(self, s: str) -> str:
        """Stack.

        Running time: O(n^2) where n is the length of s.
        """
        st = []
        
        for c in s:
            if c == '(':
                st.append('')
            elif c == ')':
                v = st.pop()[::-1]
                if st:
                    st[-1] += v
                else:
                    st.append(v)
            else:
                if st:
                    st[-1] += c
                else:
                    st.append(c)
        
        return st[0]
            