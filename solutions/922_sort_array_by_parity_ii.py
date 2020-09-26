class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        even, odd = [], []
        for a in A:
            if a % 2 == 1:
                odd.append(a)
            else:
                even.append(a)
        res = []
        for i in range(len(A)):
            if i % 2 == 1:
                res.append(odd.pop())
            else:
                res.append(even.pop())
        return res