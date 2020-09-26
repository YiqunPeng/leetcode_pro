class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        m = nums[0]
        c = 1
        for num in nums[1:]:
            if m != num:
                if c == 0:
                    m = num
                    c = 1
                else:
                    c -= 1
            else:
                c += 1
        return m
