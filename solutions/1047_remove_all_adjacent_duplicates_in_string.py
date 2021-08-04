class Solution:
    def removeDuplicates(self, S: str) -> str:
    	"""Stack.

    	Running time: O(n) where n is the length of S.
    	"""
        st = []
        for c in s:
            if not st or st[-1] != c:
                st.append(c)
            else:
                st.pop()
        return ''.join(st)
