class Solution:
    def isValid(self, s: str) -> bool:
        """Stack
        
        Running Time: O(n) where n is the length of s.
        """
        match = {')': '(', ']': '[', '}': '{'}
        o = set(['(', '[', '{'])
        st = []
        for i in s:
            if i in o:
                st.append(i)
            elif st and st[-1] == match[i]:
                st.pop()
            else:
                return False
        return not st
        