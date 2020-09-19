class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of seats.
        """
        res = 1  
        pre = None
        for i in range(len(seats)):
            if seats[i] == 1:
                if pre is None:
                    res = max(res, i)
                else:
                    res = max(res, (i - pre) // 2)
                pre = i
                
        return max(res, len(seats) - 1 - pre)