class Solution:
    def queryString(self, S: str, N: int) -> bool:
    	"""String.
    	"""
        sub = set()
        for i in range(1, min(25, len(S) + 1)):
            for j in range(len(S) + 1 - i):
                sub.add(S[j:j+i])
        for i in range(1, N + 1):
            if bin(i)[2:] not in sub:
                return False
        return True
