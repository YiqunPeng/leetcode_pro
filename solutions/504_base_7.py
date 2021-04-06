class Solution:
    def convertToBase7(self, num: int) -> str:
        s = '-' if num < 0 else ''
        num = abs(num)
        res = []
        while num != 0:
            d, m = divmod(num, 7)
            res.append(str(m))
            num = d
        return s + ''.join(res[::-1] if res else ['0'])
