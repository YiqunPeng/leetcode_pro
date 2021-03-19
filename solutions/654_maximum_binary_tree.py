class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxv, maxi = nums[0], 0
        for i, v in enumerate(nums):
            if v > maxv:
                maxv = v
                maxi = i
        left = self.constructMaximumBinaryTree(nums[:maxi])
        right = self.constructMaximumBinaryTree(nums[maxi+1:])
        node = TreeNode(maxv, left, right)
        return node
