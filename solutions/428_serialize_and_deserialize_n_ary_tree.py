"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        self._preorder(root, res)
        return ' '.join(res)
        
    def _preorder(self, root, res):
        if not root:
            return
        res.extend([str(root.val), str(len(root.children))])
        for child in root.children:
            self._preorder(child, res)
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        splits = data.split(' ')
        return self._rebuild(deque(splits))
    
    def _rebuild(self, q):
        val = int(q.popleft())
        num = int(q.popleft())
        children = []
        for i in range(num):
            child = self._rebuild(q)
            children.append(child)
        node = Node(val, children)
        return node
