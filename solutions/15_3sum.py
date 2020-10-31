class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Two pointers.

        Running time: O(n^2) where n == len(nums).
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(0, n - 2):
            if not i or nums[i] != nums[i-1]:
                l, r = i + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] == 0:
                        res.append([nums[l], nums[r], nums[i]])
                        while l < n - 1 and nums[l] == nums[l+1]:
                            l += 1
                        while r > r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] + nums[i] > 0:
                        r -= 1
                    else:
                        l += 1
        return res
