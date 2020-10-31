class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Two pointers.

        Running time: O(n^3) where n == len(nums).
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                ts = self._three_sum(nums, i + 1, target - nums[i])
                for j in ts:
                    res.append([nums[i]] + j)
        return res
    
    def _three_sum(self, nums, s, tar):
        ret = []
        for i in range(s, len(nums) - 2):
            if i == s or nums[i] != nums[i-1]:
                t = tar - nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == t:
                        ret.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l+1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < t:
                        l += 1
                    else:
                        r -= 1
        return ret
