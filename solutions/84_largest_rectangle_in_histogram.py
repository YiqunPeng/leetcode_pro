class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Stack.

        Running time: O(n) where n == len(heights).
        """
        st = []
        res = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                h = heights[st.pop()]
                w = i - 1 - st[-1]
                res = max(res, h * w)
            st.append(i)
        return res
