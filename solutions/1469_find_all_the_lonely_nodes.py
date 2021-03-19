class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                continue
            elif not (node.left and node.right):
                if node.left:
                    res.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    res.append(node.right.val)
                    q.append(node.right)
            else:
                q.append(node.left)
                q.append(node.right)
        return res
