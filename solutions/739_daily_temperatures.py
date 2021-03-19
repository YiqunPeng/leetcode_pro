class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
    	"""Stack.

    	Running time: O(n) where n == len(T).
    	"""
        res = [0] * len(T)
        st = []
        for i in range(len(T)):
            while st and T[st[-1]] < T[i]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return res
