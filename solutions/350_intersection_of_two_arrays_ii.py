class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	"""Hash table.

    	Running time: O(n) where n is the total number of elements in nums1 and nums2.
    	"""
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        
        ret = []
        
        for k, v in c1.items():
            if k in c2:
                ret.extend([k] * min(v, c2[k]))
        
        return ret