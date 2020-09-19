class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
    	"""Array.

    	Running time: O(q*m) where q is the length of queries.
    	"""
        p = [i + 1 for i in range(m)]
        res = []
        for q in queries:
            for i in range(m):
                if p[i] == q:
                    res.append(i)
                    p = [p[i]] + p[:i] + p[i+1:]
        return res
