class Solution:
    def heightChecker(self, heights: List[int]) -> int:
    	"""Running Time: O(n log n) where n is the length of heights.
    	"""
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
        