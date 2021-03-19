class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """Two pointers.
        """
        m = 10 ** 9 + 7
        c = Counter(deliciousness)
        k = sorted(c.keys())
        res = 0
        for i in range(22):
            t = 2 ** i
            l, r = 0, len(k) - 1
            while l < r:
                if k[l] + k[r] == t:
                    res = (res + c[k[r]] * c[k[l]] % m) % m
                    l += 1
                elif k[l] + k[r] < t:
                    l += 1
                else:
                    r -= 1
            if t > 1 and t // 2 in c:
                res = (res + c[t//2] * (c[t//2] - 1) // 2) % m
        return res
