class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
    	"""Sort.

    	Running time: O(aloga + blogb) where a == len(A) and b == len(B).
    	"""
        a, b = sorted(A), sorted(B, reverse=True)
        d = collections.defaultdict(list)
        for i in b:
            if a[-1] > i:
                d[i].append(a.pop())
        return [(d[i] or a).pop() for i in B]
