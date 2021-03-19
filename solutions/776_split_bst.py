class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        if root.val <= V:
            s, l = self.splitBST(root.right, V)
            root.right = s
            return [root, l]
        else:
            s, l = self.splitBST(root.left, V)
            root.left = l
            return [s, root]
