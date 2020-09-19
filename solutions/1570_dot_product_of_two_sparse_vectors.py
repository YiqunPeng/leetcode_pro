class SparseVector:
    def __init__(self, nums: List[int]):
        """Hash table.

        Running time: O(n) where n is the length of nums.
        """
        self.val_dict = {}
        for i, num in enumerate(nums):
            if num:
                self.val_dict[i] = num    

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        """Running time: O(k) where k is the number of non-zero value in nums.
        """
        res = 0
        for k, v in self.val_dict.items():
            if k in vec.val_dict:
                res += v * vec.val_dict[k]
        return res
