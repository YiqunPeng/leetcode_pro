class Solution:
    def trap(self, height: List[int]) -> int:
        """Two pointer.

        Running time: O(n) where n == len(height).
        """
        if not height:
            return 0
        res = 0
        l, r = 0, len(height) - 1
        while l + 1 < r:
            if height[l] <= height[r]:
                res += max(0, height[l] - height[l+1])
                height[l+1] = max(height[l+1], height[l])
                l += 1
            else:
                res += max(0, height[r] - height[r-1])
                height[r-1] = max(height[r], height[r-1])
                r -= 1
        return res
