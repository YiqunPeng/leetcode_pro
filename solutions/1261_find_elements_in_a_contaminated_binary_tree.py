class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        q = deque([root])
        root.val = 0
        while q:
            n = q.popleft()
            self.values.add(n.val)
            if n.left:
                n.left.val = n.val * 2 + 1
                q.append(n.left)
            if n.right:
                n.right.val = n.val * 2 + 2
                q.append(n.right)

    def find(self, target: int) -> bool:
        return target in self.values
