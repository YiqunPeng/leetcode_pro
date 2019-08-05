class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """Stack.

        Running time: O(n) where n is the length of S.
        """
        st = []
        ret = 0
        for s in S:
            if s == '(':
                st.append(0)
            else:
                v = st.pop()
                if st:
                    st[-1] += max(1, v * 2)
                else:
                    ret += max(1, v * 2)
                    
        return ret
