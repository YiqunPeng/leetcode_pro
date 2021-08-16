class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
    	"""Stack.
    	"""
        mod = 10 ** 9 + 7
        res = 0
        A = [0] + A + [0]
        n = len(A)
        st = []
        for i in range(n):
            while st and A[st[-1]] > A[i]:
                idx = st.pop()
                res += A[idx] * (i - idx) * (idx - st[-1]) % mod
            st.append(i)
        return res % mod
