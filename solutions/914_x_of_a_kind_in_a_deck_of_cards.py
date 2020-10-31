class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
    	"""GCD.
    	"""
        v = collections.Counter(deck).values()
        return reduce(self._gcd, v) > 1
    
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
