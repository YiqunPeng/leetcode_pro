class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """Stack.

        Running time: O(n) where n is the length of S.
        """
        st = [0]
        for s in S:
            if s == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(1, 2 * v)
        return st[0]
