class Solution:
    def isValid(self, s: str) -> bool:
        """Stack
        
        Running Time: O(n) where n is the length of s.
        """
        sym = {
            '(': -1, ')': 1,
            '[': -2, ']': 2,
            '{': -3, '}': 3
        }
        
        st = []
        for c in s:
            if sym[c] < 0:
                st.append(sym[c])
            else:
                if not st or st[-1] + sym[c] != 0:
                    return False
                st.pop()
                
        return not st
        