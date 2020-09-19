class Solution:
    def countPrimes(self, n: int) -> int:
        """Math.

        Running time: O(n log log n).
        """
        nums = [1] * n
        
        i = 2
        while i * i < n:
            j = i * i
            if nums[j] != 0:
                while j < n:
                    nums[j] = 0
                    j += i
            i += 1
        
        return sum(nums[2:])