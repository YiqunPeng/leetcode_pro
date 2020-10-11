class Solution:
    def maximumSwap(self, num: int) -> int:
        """Array.

        Running time: O(n) where n == len(num).
        """
        nums = list(str(num))
        n = len(nums)
        m = list(range(n))
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[m[i+1]]:
                m[i] = i
            else:
                m[i] = m[i+1]
        for i in range(n - 1):
            if nums[i] < nums[m[i+1]]:
                nums[i], nums[m[i+1]] = nums[m[i+1]], nums[i]
                break
        return int(''.join(nums)) 
