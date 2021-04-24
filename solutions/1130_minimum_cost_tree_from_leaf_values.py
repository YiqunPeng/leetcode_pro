class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        st = [16]
        res = 0
        for a in arr:
            while st[-1] <= a:
                v = st.pop()
                res += v * min(a, st[-1])
            st.append(a)
        while len(st) > 2:
            res += st.pop() * st[-1]
        return res
