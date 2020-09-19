class Solution:
    def romanToInt(self, s: str) -> int:
        """Stack.

        Running time: O(n) where n is the length of s.
        """
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = 0
        st = []
        
        for c in s:
            while st and symbols[c] > symbols[st[-1]]:
                res -= symbols[st.pop()]
            st.append(c)
            
        while st:
            res += symbols[st.pop()]
        return res
            