class Solution:
    def sumRootToLeaf(self, root: TreeNode, v=0, s=0) -> int:
        if not root:
            return s
        v = v << 1 | root.val
        if not root.left and not root.right:
            return s + v
        return s + self.sumRootToLeaf(root.left, v, s) + self.sumRootToLeaf(root.right, v, s)
