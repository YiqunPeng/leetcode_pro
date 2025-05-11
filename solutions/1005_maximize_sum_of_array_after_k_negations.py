class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(k):
            n = heappop(nums)
            heappush(nums, -n)
        return sum(nums)