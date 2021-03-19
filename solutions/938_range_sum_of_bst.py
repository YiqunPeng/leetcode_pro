class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self._sum(root, 0, low, high)
    
    def _sum(self, node, s, low, high):
        if not node:
            return s
        if node.val < low:
            return self._sum(node.right, s, low, high)
        elif node.val > high:
            return self._sum(node.left, s, low, high)
        else:
            return node.val + self._sum(node.left, s, low, high) + self._sum(node.right, s, low, high)
