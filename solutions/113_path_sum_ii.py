class Solution:
    
    def __init__(self):
        self.res = []
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self._find_all_paths(root, targetSum, [])
        return self.res
    
    def _find_all_paths(self, root, tgt, path):
        if not root:
            if not tgt and path:
                self.res.append(path)
            return
        if not root.left and not root.right:
            if tgt == root.val:
                self.res.append(path + [root.val])
            return
        if root.left:
            self._find_all_paths(root.left, tgt - root.val, path + [root.val])
        if root.right:
            self._find_all_paths(root.right, tgt - root.val, path + [root.val])
