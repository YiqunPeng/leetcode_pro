class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
