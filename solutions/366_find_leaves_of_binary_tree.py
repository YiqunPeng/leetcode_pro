class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        self._dfs(root, res)
        return res
    
    def _dfs(self, node, res):
        if not node:
            return -1
        l = self._dfs(node.left, res)
        r = self._dfs(node.right, res)
        d = max(l, r) + 1
        if len(res) < d + 1:
            res.append([node.val])
        else:
            res[d].append(node.val)
        return d
