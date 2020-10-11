class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        """Array.
        
        Running time: O(n) where n is the length of calories.
        """
        t = sum(calories[:k-1])
        res = 0
        for i in range(k-1, len(calories)):
            t += calories[i]
            if t < lower:
                res -= 1
            elif t > upper:
                res += 1
            t -= calories[i+1-k]
        return res
