class Solution:
    def increasingBST(self, root: TreeNode, nxt = None) -> TreeNode:
        if not root:
            return nxt
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, nxt)
        return res
