class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])
        seen = set()
        while q:
            node = q.popleft()
            if node.right:
                if node.right.right in seen:
                    node.right = None
                    return root
                q.append(node.right)
                seen.add(node.right)
            if node.left:
                if node.left.right in seen:
                    node.left = None
                    return root
                q.append(node.left)
                seen.add(node.left)
