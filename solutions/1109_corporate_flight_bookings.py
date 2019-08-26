class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    	"""Math.

    	Running time: O(n) where n is the length of bookings.
    	"""
        seats = [0] * (n + 2)
        
        for i, j, k in bookings:
            seats[i] += k
            seats[j+1] -= k
            
        for i in range(2, n + 1):
            seats[i] += seats[i-1]
        
        return seats[1:-1]