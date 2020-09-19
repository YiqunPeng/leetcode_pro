class Solution:
    def rob(self, root: TreeNode) -> int:
        """DP.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        def dfs(node):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                return 0, node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return max(left) + max(right), left[0] + right[0] + node.val
        
        return max(dfs(root))