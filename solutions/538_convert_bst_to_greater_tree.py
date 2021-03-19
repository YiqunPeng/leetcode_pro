class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self._convert(root, 0)
        return root
    
    def _convert(self, root, s):
        if not root:
            return s
        if root.right:
            s = self._convert(root.right, s)
        root.val += s
        s = root.val
        if root.left:
            s = self._convert(root.left, s)
        return s
