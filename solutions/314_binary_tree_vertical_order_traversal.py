class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, pos = q.popleft()
            d[pos].append(node.val)
            if node.left:
                q.append((node.left, pos - 1))
            if node.right:
                q.append((node.right, pos + 1))
        res = []
        for k in sorted(d):
            res.append(d[k])
        return res
