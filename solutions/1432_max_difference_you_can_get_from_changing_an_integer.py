class Solution:
    def maxDiff(self, num: int) -> int:
        """String.

        Running time: O(len(str(num))).
        """
        nums = list(str(num))
        min_v, max_v = None, None
        for i in range(len(nums)):
            if i == 0 and nums[0] != '1':
                v = nums[0]
                for j in range(len(nums)):
                    if nums[j] == v:
                        nums[j] = '1'
                break
            elif i > 0 and nums[i] != nums[0] and nums[i] != '0':
                v = nums[i]
                for j in range(i, len(nums)):
                    if nums[j] == v:
                        nums[j] = '0'
                break
        min_v = int(''.join(nums))
        nums = list(str(num))        
        for i in range(len(nums)):
            if nums[i] != '9':
                v = nums[i]
                for j in range(i, len(nums)):
                    if nums[j] == v:
                        nums[j] = '9'
                break
        max_v = int(''.join(nums))
        return max_v - min_v
