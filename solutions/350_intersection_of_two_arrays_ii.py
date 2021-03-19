class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	"""Hash table.

    	Running time: O(n) where n is the total number of elements in nums1 and nums2.
    	"""
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for k1, v1 in c1.items():
            if k1 in c2:
                res.extend([k1] * min(v1, c2[k1]))
        return res
