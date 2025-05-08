class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        w = 0
        res = 0
        for wei in weight:
            if w + wei <= 5000:
                w += wei
                res += 1
            else:
                break
        return res