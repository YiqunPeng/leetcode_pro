# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = self.preorder(root)
        return ' '.join(nodes)

    def preorder(self, root):
        if not root:
            return ['#']
        l = self.preorder(root.left)
        r = self.preorder(root.right)
        return [str(root.val)] + l + r

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = data.split(' ')
        return self.decode(deque(nodes))

    def decode(self, nodes):
        if nodes[0] == '#':
            nodes.popleft()
            return None
        
        n = TreeNode(int(nodes[0]))
        nodes.popleft()
        n.left = self.decode(nodes)
        n.right = self.decode(nodes)
        return n