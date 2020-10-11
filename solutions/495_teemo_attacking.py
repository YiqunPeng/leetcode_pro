class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of timeSeries.
    	"""
        if not timeSeries:
            return 0
        res = 0
        n = len(timeSeries)
        for i in range(0, n - 1):
            res += min(duration, timeSeries[i+1] - timeSeries[i])
        return res + duration
