class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self._dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def _dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return head.val == root.val and (self._dfs(head.next, root.left) or self._dfs(head.next, root.right))
