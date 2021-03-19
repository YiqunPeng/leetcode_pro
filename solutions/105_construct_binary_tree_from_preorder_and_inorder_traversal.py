class Solution:
    
    def __init__(self):
        self.pre_idx = 0
        self.d = {}
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for i in range(len(inorder)):
            self.d[inorder[i]] = i
        return self._build(preorder, inorder, 0, len(preorder))
        
    def _build(self, preorder, inorder, start, end):
        if start == end:
            return None
        idx = self.d[preorder[self.pre_idx]]
        root = TreeNode(preorder[self.pre_idx])
        self.pre_idx += 1
        root.left = self._build(preorder, inorder, start, idx)
        root.right = self._build(preorder, inorder, idx + 1, end)
        return root
