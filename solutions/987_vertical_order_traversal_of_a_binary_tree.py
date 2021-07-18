class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        cols = defaultdict(list)
        q = deque()
        q.append((root, 0, 0))
        while q:
            node, row, col = q.popleft()
            cols[col].append((row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        res = []
        for k in sorted(cols):
            res.append([i[1] for i in sorted(cols[k])])
        return res
