class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
    	"""Hash set.

    	Running time: O(n) where n == len(A).
    	"""
        s = set()
        for a in A:
            if a in s:
                return a
            s.add(a)
