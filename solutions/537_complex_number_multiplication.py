class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
    	"""String.
    	"""
        ar, ai = self._get(a)
        br, bi = self._get(b)
        r = ar * br - ai * bi
        i = ar * bi + br * ai
        return str(r) + '+' + str(i) + 'i'
        
    def _get(self, n):
        p = n.split('+')
        return int(p[0]), int(p[1][:-1])
