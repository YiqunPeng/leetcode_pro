class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root or self._postorder(root, 0, limit):
            return None
        else:
            return root
        
    def _postorder(self, root, s, limit):
        if not root.left and not root.right:
            return s + root.val < limit
        ldel, rdel = True, True
        if root.left:
            ldel = self._postorder(root.left, s + root.val, limit)
            if ldel:
                root.left = None
        if root.right:
            rdel = self._postorder(root.right, s + root.val, limit)
            if rdel:
                root.right = None
        return ldel and rdel
