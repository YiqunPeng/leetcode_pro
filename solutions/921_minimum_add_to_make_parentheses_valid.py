class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """Stack.

        Running time: O(n) where n is the length S.
        """
        st = []
        
        for c in S:
            if not st:
                st.append(c)
            elif c == '(':
                st.append(c)
            else:
                if st[-1] == '(':
                    st.pop()
                else:
                    st.append(c)
                    
        return len(st)
