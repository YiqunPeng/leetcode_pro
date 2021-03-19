class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        h = 0
        n = 0
        while n < label:
            n += 2 ** h
            h += 1
        h -= 1
        res = []
        while label != 1:
            res.append(label)
            lmin = 2 ** (h - 1)
            lmax = 2 ** h - 1
            label = lmin + lmax - label // 2
            h -= 1
        res.append(1)
        return res[::-1]
