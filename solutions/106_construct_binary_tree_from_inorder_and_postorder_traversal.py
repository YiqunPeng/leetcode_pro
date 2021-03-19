class Solution:
    
    def __init__(self):
        self.inorder_p = {}
        self.postorder_idx = None
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder_idx = len(postorder) - 1
        for i, v in enumerate(inorder):
            self.inorder_p[v] = i
        return self._build(inorder, postorder, 0, len(inorder))
    
    def _build(self, inorder, postorder, start, end):
        if start == end:
            return None
        idx = self.inorder_p[postorder[self.postorder_idx]]
        root = TreeNode(postorder[self.postorder_idx])
        self.postorder_idx -= 1
        root.right = self._build(inorder, postorder, idx+1, end)
        root.left = self._build(inorder, postorder, start, idx)
        return root
