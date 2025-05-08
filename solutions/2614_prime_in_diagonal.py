class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        for i in range(len(nums)):
            if self._is_prime(nums[i][i]):
                res = max(res, nums[i][i])
            if self._is_prime(nums[i][len(nums)-i-1]):
                res = max(res, nums[i][len(nums)-i-1])
        return res

    def _is_prime(self, num):
        if num == 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True