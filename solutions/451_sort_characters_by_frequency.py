class Solution:
    def frequencySort(self, s: str) -> str:
    	"""Hash table.

    	Running time: O(nlogn) where n == len(s).
    	"""
        c = collections.Counter(s)
        res = []
        for k, v in sorted(c.items(), key=lambda x:x[1], reverse=True):
            res.extend([k] * v)
        return ''.join(res)
