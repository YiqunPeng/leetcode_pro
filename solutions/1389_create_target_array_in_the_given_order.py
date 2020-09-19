class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of index.
    	"""
        res = []
        for i in range(len(index)):
            if index[i] == 0:
                res = [nums[i]] + res
            else:
                res = res[:index[i]] + [nums[i]] + res[index[i]:]
        return res
