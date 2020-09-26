class Solution:
    def average(self, salary: List[int]) -> float:
    	"""Array.

    	Running time: O(n) where n is the length of salary.
    	"""
        n = len(salary)
        min_s, max_s = min(salary), max(salary)
        return (sum(salary) - min_s - max_s) / float(n - 2)
