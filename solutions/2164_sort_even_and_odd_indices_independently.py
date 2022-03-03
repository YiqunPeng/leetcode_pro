class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e, o = [], []
        for i in range(len(nums)):
            if i % 2:
                o.append(nums[i])
            else:
                e.append(nums[i])
        e.sort(reverse=True)
        o.sort()
        res = []
        for i in range(len(nums)):
            if i % 2:
                res.append(o.pop())
            else:
                res.append(e.pop())
        return res
    