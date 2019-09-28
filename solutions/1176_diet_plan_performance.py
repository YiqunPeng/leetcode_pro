class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        """Array.
        
        Running time: O(n) where n is the length of calories.
        """
        t = 0
        for i in range(k):
            t += calories[i]
        
        if t < lower:
            ret = -1
        elif t > upper:
            ret = 1
        else:
            ret = 0
           
        for i in range(k, len(calories)):
            t = t - calories[i-k] + calories[i]
            if t < lower:
                ret -= 1
            elif t > upper:
                ret += 1
        
        return ret
