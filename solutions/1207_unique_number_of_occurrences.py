class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
    	"""Hash set.

    	Running time: O(n) where n == len(arr).
    	"""
        c = collections.Counter(arr)
        return len(set(c.values())) == len(c.values())
