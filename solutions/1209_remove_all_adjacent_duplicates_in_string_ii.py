class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """Stack.

        Running time: O(n) where n is the length of s.
        """
        st = [['#', 0]]
        for c in s:
            if st[-1][0] == c:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([c, 1])
        return ''.join([i[0] * i[1] for i in st])
