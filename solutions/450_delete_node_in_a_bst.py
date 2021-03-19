class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            return self._delete_root(root)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def _find_min(self, root):
        while root and root.left:
            root = root.left
        return root
    
    def _delete_root(self, root):
        if not root:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        node = self._find_min(root.right)
        node.left = root.left
        return root.right
