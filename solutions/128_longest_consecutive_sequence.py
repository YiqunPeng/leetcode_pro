class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in nums:
                l = 1
                cur_n = n

                while cur_n + 1 in nums:
                    l += 1
                    cur_n += 1
                
                res = max(res, l)
        
        return res