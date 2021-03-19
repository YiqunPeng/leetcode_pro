class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        px, dx, fx = None, None, False
        py, dy, fy = None, None, False
        q = deque([(root, 0)])
        while q:
            node, d = q.popleft()
            if not fx and node.left and node.left.val == x or node.right and node.right.val == x:
                px, dx, fx = node, d + 1, True
            if not fy and node.left and node.left.val == y or node.right and node.right.val == y:
                py, dy, fy = node, d + 1, True
            if fx and fy:
                return dx == dy and px != py
            if node.left:
                q.append((node.left, d + 1))
            if node.right:
                q.append((node.right, d + 1))
