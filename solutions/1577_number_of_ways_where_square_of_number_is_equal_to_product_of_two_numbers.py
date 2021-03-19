class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """Hash table.
        """
        res = 0
        d1 = collections.Counter([i*i for i in nums1])
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                v = nums2[i] * nums2[j]
                if v in d1:
                    res += d1[v]
        d2 = collections.Counter([i*i for i in nums2])
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                v = nums1[i] * nums1[j]
                if v in d2:
                    res += d2[v]
        return res
