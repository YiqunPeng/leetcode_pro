class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root.val < val:
            return TreeNode(val, root)
        self._insert(root, val)
        return root
    
    def _insert(self, root, val):
        if not root.right or root.right.val < val:
            root.right = TreeNode(val, root.right)
            return root
        self._insert(root.right, val)
