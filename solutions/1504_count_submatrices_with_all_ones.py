class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        m, n = len(mat), len(mat[0])
        h = [0] * n
        for i in range(m):
            for j in range(n):
                h[j] = 0 if mat[i][j] == 0 else h[j] + 1
            res += self._count_row(h)
        return res
    
    def _count_row(self, h):
        s = [0] * len(h)
        st = []
        for i in range(len(h)):
            if h[i] == 0:
                st = [i]
                continue
            while st and h[st[-1]] >= h[i]:
                st.pop()
            if st:
                p = st[-1]
                s[i] = s[p] + h[i] * (i - p)
            else:
                s[i] = h[i] * (i + 1)
            st.append(i)
        return sum(s)
