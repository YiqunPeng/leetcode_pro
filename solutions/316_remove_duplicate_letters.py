class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Stack.

        Running time: O(n) where n == len(s).
        """
        d = {c: i for i, c in enumerate(s)}
        st = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                continue
            while st and st[-1] > c and d[st[-1]] > i:
                v = st.pop()
                seen.remove(v)
            st.append(c)
            seen.add(c)
        return ''.join(st)
