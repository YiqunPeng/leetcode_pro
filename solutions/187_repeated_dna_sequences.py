class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
    	"""Hash set.
    	"""
        seq = set([s[:10]])
        res = set()
        for i in range(1, len(s) - 9):
            if s[i:i+10] in seq:
                res.add(s[i:i+10])
            seq.add(s[i:i+10])
        return list(res)
