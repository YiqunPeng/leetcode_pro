class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """Tree.
        """
        nodes = deque([root])
        res = 0
        while nodes:
            n = nodes.popleft()
            if n.val % 2 == 0:
                if n.left:
                    if n.left.left:
                        res += n.left.left.val
                    if n.left.right:
                        res += n.left.right.val
                if n.right:
                    if n.right.left:
                        res += n.right.left.val
                    if n.right.right:
                        res += n.right.right.val
            if n.left:
                nodes.append(n.left)
            if n.right:
                nodes.append(n.right)
        return res
