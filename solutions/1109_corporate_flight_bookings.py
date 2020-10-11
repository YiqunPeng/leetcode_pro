class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of bookings.
    	"""
        b = [0] * n
        for s, e, v in bookings:
            b[s-1] += v
            if e < n:
                b[e] -= v
        for i in range(1, n):
            b[i] += b[i-1]
        return b