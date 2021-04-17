class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        for i in range(1, min(num, int(num ** 0.5) + 1)):
            if num % i == 0:
                s += i + num // i
        return s == num * 2
