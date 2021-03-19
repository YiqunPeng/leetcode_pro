class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        cur = leaf
        pre = None
        while cur != root:
            if cur.left:
                cur.right = cur.left
            if cur == cur.parent.left:
                cur.parent.left = None
            else:
                cur.parent.right = None
            cur.left = cur.parent
            cur.parent = pre
            pre = cur
            cur = cur.left
        root.parent = pre    
        return leaf
