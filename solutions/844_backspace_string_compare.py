class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self._process(s) == self._process(t)
    
    def _process(self, s):
        st = []
        for c in s:
            if c == '#':
                if st:
                    st.pop()
            else:
                st.append(c)
        return st
