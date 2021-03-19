class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self._preorder(root, res)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(' '))
        return self._decode(values)
        
    def _preorder(self, root, res):
        if root:
            res.append(str(root.val))
            self._preorder(root.left, res)
            self._preorder(root.right, res)
        else:
            res.append('#')
            
    def _decode(self, values):
        v = next(values)
        if v == '#':
            return None
        root = TreeNode(int(v))
        root.left = self._decode(values)
        root.right = self._decode(values)
        return root
