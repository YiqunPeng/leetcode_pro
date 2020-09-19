class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Hash table.

        Running time: O(n) where n is the length of nums.
        """
        n = len(nums)
        
        re = {0: -1}
        s = 0
        
        for i, num in enumerate(nums):
            s += num
            r = s % k if k else s
            if r in re:
                if i - re[r] >= 2:
                    return True
            else:
                re[r] = i

                
        return False