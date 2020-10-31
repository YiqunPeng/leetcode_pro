class Solution:
    def thousandSeparator(self, n: int) -> str:
    	"""String.
    	"""
        res = ''
        n = str(n)
        for i in range(len(n)):
            res += n[i]
            if i != len(n) - 1 and (len(n) - i - 1) % 3 == 0:
                res += '.'
        return res
