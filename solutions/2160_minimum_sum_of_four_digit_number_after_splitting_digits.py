class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [num // 1000, num // 100 % 10, num // 10 % 10, num % 10]
        digits.sort()
        return digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3]
