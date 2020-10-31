class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        res = []
        if not nums:
            return res
        s, e = 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1 or i == len(nums) - 1:
                if s == e:
                    res.append(str(nums[s]))
                else:
                    res.append(str(nums[s]) + '->' + str(nums[e]))
                s = e = i
            else:
                e += 1
        if s == e:
            res.append(str(nums[s]))
        else:
            res.append(str(nums[s]) + '->' + str(nums[e]))
        return res
