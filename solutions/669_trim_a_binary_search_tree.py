class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        while root and not (low <= root.val <= high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        if not root:
            return None
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
