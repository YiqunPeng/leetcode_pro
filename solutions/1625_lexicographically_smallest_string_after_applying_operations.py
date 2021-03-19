class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res = s
        seen = set(res)
        q = deque([s])
        while q:
            v = q.popleft()
            va = self._apply_a(v, a)
            vb = self._apply_b(v, b)
            if va not in seen:
                seen.add(va)
                q.append(va)
            if vb not in seen:
                seen.add(vb)
                q.append(vb)
            res = min(res, va, vb)
        return res
    
    def _apply_a(self, v, a):
        v = list(v)
        for i in range(len(v)):
            if i % 2 == 1:
                n = (int(v[i]) + a) % 10
                v[i] = str(n)
        return ''.join(v)
    
    def _apply_b(self, v, b):
        return v[-b:] + v[:-b]
