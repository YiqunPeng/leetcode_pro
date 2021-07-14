class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Two pointers.

        Running time: O(n^3) where n == len(nums).
        """
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i and nums[i-1] == nums[i]:
                continue
            triplets = self._3sum(nums[i+1:], target - nums[i])
            for t in triplets:
                res.append([nums[i]] + t)
        return res
    
    def _3sum(self, nums, t):
        res = []
        for i in range(len(nums)-2):
            if i and nums[i-1] == nums[i]:
                continue
            pairs = self._2sum(nums[i+1:], t - nums[i])
            for p in pairs:
                res.append([nums[i]] + p)
        return res
    
    def _2sum(self, nums, t):
        res = []
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == t:
                res.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > t:
                r -= 1
            else:
                l += 1
        return res
