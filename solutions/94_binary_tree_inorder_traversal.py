class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    prev.right = None
                    root = root.right
        return res
