class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        idx = (len(nums) - 1) // 2
        node = TreeNode(nums[idx], self.sortedArrayToBST(nums[:idx]), self.sortedArrayToBST(nums[idx+1:]))
        return node
