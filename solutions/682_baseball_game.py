class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = []
        for op in ops:
            if op == '+':
                st.append(st[-1] + st[-2])
            elif op == 'D':
                st.append(st[-1] * 2)
            elif op == 'C':
                st.pop()
            else:
                st.append(int(op))
        return sum(st)