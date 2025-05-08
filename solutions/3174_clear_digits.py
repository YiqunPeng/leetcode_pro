class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if '0' <= c <= '9':
                if st:
                    st.pop()
                else:
                    st.append(c)
            else:
                st.append(c)
        return ''.join(st)