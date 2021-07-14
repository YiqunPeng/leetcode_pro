class Solution:
    
    def __init__(self):
        self.s = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        self._convert(root)
        return root
    
    def _convert(self, root):
        if not root:
            return
        self._convert(root.right)
        v = root.val
        root.val += self.s
        self.s += v
        self._convert(root.left)
