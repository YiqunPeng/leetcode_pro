class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)
        a, b, ca, cb = 0, 1, 0, 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
            elif ca == 0:
                a = num
                ca = 1
            elif cb == 0:
                b = num
                cb = 1
            else:
                ca -= 1
                cb -= 1
        res = [i for i in [a, b] if (nums.count(i) > len(nums) // 3)]
        return res
