class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            p = abs(nums[i]) - 1
            if nums[p] > 0:
                nums[p] *= -1    
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
  