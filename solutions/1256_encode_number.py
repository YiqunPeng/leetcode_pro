class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""
        k = 1
        while num > 2 ** k:
            num -= 2 ** k
            k += 1
        v = []
        num -= 1
        while num != 0:
            v.append(str(num % 2))
            num //= 2
        v += ['0'] * (k - len(v))
        return ''.join(v[::-1])
