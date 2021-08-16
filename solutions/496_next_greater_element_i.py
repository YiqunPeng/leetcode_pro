class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Stack.

        Running time: O(n1 + n2) where n1 == len(nums1) and n2 == len(nums2).
        """
        d = defaultdict(lambda: -1)
        st = []
        for num in nums2:
            while st and st[-1] < num:
                val = st.pop()
                d[val] = num
            st.append(num)
        res = []
        for num in nums1:
            res.append(d[num])
        return res
