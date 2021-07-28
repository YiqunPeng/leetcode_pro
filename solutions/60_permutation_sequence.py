class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = i * factorial[i-1]
        nums = list(range(1, n + 1))
        m = n - 1
        res = ''
        k -= 1
        while nums:
            gnum = factorial[m]
            idx = k // gnum
            res += str(nums[idx])
            nums.pop(idx)
            m -= 1
            k = k - idx * gnum
        return res
