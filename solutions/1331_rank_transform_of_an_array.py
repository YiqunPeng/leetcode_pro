class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(nlogn) where n is the length of arr.
    	"""
        sarr = set(arr)
        s = sorted(list(sarr))
        d = {s[i] : i + 1 for i in range(len(s))}
        res = []
        for a in arr:
            res.append(d[a])
        return res
