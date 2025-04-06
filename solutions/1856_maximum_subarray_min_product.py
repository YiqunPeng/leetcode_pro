class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        res = 0
        st = []
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                p = st.pop()
                n_top = st[-1] if st else -1
                res = max(res, nums[p] * (pre_sum[i] - pre_sum[n_top + 1]))
            st.append(i)

        return res % (10**9 + 7)
