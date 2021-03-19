class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        q = deque([(root, 1)])
        while q:
            length = len(q)
            leftmost = q[0][1]
            rightmost = q[-1][1]
            res = max(res, rightmost - leftmost + 1)
            for i in range(length):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, pos * 2))
                if node.right:
                    q.append((node.right, pos * 2 + 1))
        return res
