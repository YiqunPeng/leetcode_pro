class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self._get_leaves(root1, []) == self._get_leaves(root2, [])
    
    def _get_leaves(self, root, leaves):
        if not root:
            return leaves
        if not root.left and not root.right:
            leaves.append(root.val)
            return leaves
        leaves = self._get_leaves(root.left, leaves)
        leaves = self._get_leaves(root.right, leaves)
        return leaves
