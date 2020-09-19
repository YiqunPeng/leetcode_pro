class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """DFS.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        def dfs(node):
            if not node:
                return 0
    
            d = max(dfs(node.left), dfs(node.right)) + 1
            if d > len(res):
                res.append([node.val])
            else:
                res[d-1].append(node.val)
            return d
        
        res = []
        dfs(root)
        return res