class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = []
        d = defaultdict(int)
        i = 0
        while i < len(formula):
            c = formula[i]
            if c == '(':
                i += 1
                st.append(d)
                d = defaultdict(int)
            elif c == ')':
                i += 1
                v = 0
                while i < len(formula) and '0' <= formula[i] <= '9':
                    v = v * 10 + int(formula[i])
                    i += 1
                v = max(1, v)
                temp = st.pop()
                for k in d:
                    temp[k] += d[k] * v
                d = temp
            else:
                idx = i
                if 'A' <= c <= 'Z':
                    i += 1
                    while i < len(formula) and 'a' <= formula[i] <= 'z':
                        i += 1
                name = formula[idx:i]
                val = 0
                idx = i
                while i < len(formula) and '0' <= formula[i] <= '9':
                    val = val * 10 + int(formula[i])
                    i += 1
                val = max(1, val)
                d[name] += val
        res = ''
        for k in sorted(d):
            if d[k] > 1:
                res = res + k + str(d[k])
            else:
                res = res + k
        return res
