class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n + diff in s and n + diff * 2 in s:
                res += 1
        return res