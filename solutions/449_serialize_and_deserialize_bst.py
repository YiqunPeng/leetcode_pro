class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        self._preorder(root, res)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        preorder = [int(i) for i in data.split(',')]
        inorder = sorted(preorder)
        return self._construct_tree(preorder, inorder)
    
    def _preorder(self, root, res):
        if not root:
            return
        res.append(str(root.val))
        self._preorder(root.left, res)
        self._preorder(root.right, res)
        
    def _construct_tree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self._construct_tree(preorder[1:1+idx], inorder[:idx])
        root.right = self._construct_tree(preorder[1+idx:], inorder[idx+1:])
        return root
