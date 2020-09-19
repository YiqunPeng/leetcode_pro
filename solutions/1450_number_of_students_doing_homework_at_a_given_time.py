class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of startTime.
    	"""
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res
