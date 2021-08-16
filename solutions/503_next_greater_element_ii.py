class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """Stack.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)
        nums = nums * 2
        res = [-1] * n
        st = []
        for i in range(2 * n):
            while st and nums[st[-1]] < nums[i % n]:
                idx = st.pop()
                res[idx] = nums[i % n]
            st.append(i % n)
        return res
