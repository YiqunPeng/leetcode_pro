class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if not t1 or not t2:
            return t1 or t2
        t1.val += t2.val
        q = deque([(t1, t2)])
        while q:
            n1, n2 = q.popleft()
            if n1.left and n2.left:
                n1.left.val += n2.left.val
                q.append((n1.left, n2.left))
            if not n1.left and n2.left:
                n1.left = n2.left
            if n1.right and n2.right:
                n1.right.val += n2.right.val
                q.append((n1.right, n2.right))
            if not n1.right and n2.right:
                n1.right = n2.right
        return t1
