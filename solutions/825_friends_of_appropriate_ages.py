class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        import bisect

        ages.sort()
        
        f = 0
        last = 0
        
        for i in range(len(ages)):
            if i and ages[i] == ages[i-1]:
                f += last
                continue
                
            t = 0.5 * ages[i] + 7
            l = bisect.bisect_right(ages, t)
            r = bisect.bisect_right(ages, ages[i])
            last = max(r - l - 1, 0) 
            f += last
            
        return f
