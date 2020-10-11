class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [1]
        for i in range(k, 0, -1):
            if len(res) % 2 == 1:
                v = res[-1] + i
            else:
                v = res[-1] - i
            res.append(v)
        return res + [i for i in range(k + 2, n + 1)]
