class Solution:
    def tree2str(self, t: TreeNode) -> str:
        s = self._preorder(t, [])
        return ''.join(s[1:-1])
    
    def _preorder(self, root, s):
        if not root:
            return s
        s += ['(', str(root.val)]
        if root.left:
            s = self._preorder(root.left, s)
        if root.right:
            if not root.left:
                s += ['()']
            s = self._preorder(root.right, s)
        s.append(')')
        return s
