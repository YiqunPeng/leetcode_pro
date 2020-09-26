class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of A.
    	"""
        odd, even = [], []
        for a in A:
            if a % 2 == 1:
                odd.append(a)
            else:
                even.append(a)
        return even + odd
