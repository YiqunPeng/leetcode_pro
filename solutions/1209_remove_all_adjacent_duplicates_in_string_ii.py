class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """Stack.

        Running time: O(n) where n is the length of s.
        """
        st = []
        
        for c in s:
            if not st or st[-1][0] != c:
                st.append(c)
            elif st[-1][0] == c:
                if len(st[-1]) + 1 < k:
                    st[-1] += c
                else:
                    st.pop()
        
        return ''.join(st)
