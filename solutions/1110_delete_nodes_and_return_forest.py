class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_del = set(to_delete)
        if root.val not in to_del:
            res.append(root)
        self._post_order(root, res, to_del)
        return res
    
    def _post_order(self, root, res, to_del):
        if not root:
            return 
        root.left = self._post_order(root.left, res, to_del)
        root.right = self._post_order(root.right, res, to_del)
        if root.val in to_del:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        return root
