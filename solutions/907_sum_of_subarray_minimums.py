class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        st = []
        res = 0
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                p = st.pop()
                n_top = st[-1] if st else -1
                res += arr[p] * (p - n_top) * (i - p)
            st.append(i)
        return res % (10 ** 9 + 7)