class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """Stack.

        Running time: O(n) where n == len(preorder).
        """
        st = []
        low = float('-inf')
        for v in preorder:
            if v < low:
                return False
            while st and st[-1] < v:
                low = st.pop()
            st.append(v)
        return True
