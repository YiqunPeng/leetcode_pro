class Solution:
    def findCelebrity(self, n: int) -> int:
    	"""Array.

    	Running time: O(n).
    	"""
        candid = 0
        for i in range(1, n):
            if knows(candid, i):
                candid = i
        for i in range(n):
            if candid != i and (not knows(i, candid) or knows(candid, i)):
                return -1
        return candid
