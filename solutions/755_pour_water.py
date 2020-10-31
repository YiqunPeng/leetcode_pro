class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        """Array.

        Running time: O(n * V) where n == len(heights).
        """
        j = K
        for i in range(V):
            while j > 0 and heights[j] >= heights[j-1]:
                j -= 1
            while j < len(heights) - 1 and heights[j] >= heights[j+1]:
                j += 1
            while j > K and heights[j] == heights[j-1]:
                j -= 1
            heights[j] += 1
        return heights
