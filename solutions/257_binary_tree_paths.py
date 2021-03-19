class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self._traverse(root, '', res)
        return res
    
    def _traverse(self, root, path, res):
        if not root:
            return 
        if not root.left and not root.right:
            res.append(path + str(root.val))
            return 
        path += str(root.val) + '->'
        self._traverse(root.left, path, res)
        self._traverse(root.right, path, res)
