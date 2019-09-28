class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	"""Hash set.

    	Running time: O(n) where n is the total number of items in nums1 and nums2.
    	"""
        return list(set(nums1) & set(nums2))