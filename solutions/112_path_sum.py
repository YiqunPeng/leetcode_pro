class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        res = False
        if root.left:
            res = self.hasPathSum(root.left, targetSum - root.val)
        if not res and root.right:
            res = self.hasPathSum(root.right, targetSum - root.val)
        return res
