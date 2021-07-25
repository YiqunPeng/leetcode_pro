class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [n-1]
        max_h = heights[n-1]
        for i in range(n-2, -1, -1):
            if heights[i] > max_h:
                res.append(i)
                max_h = heights[i]
        return res[::-1]
