class Solution:
    
    def __init__(self):
        self.res = []
        self.subtrees = defaultdict(int)
    
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self._post_order(root)
        return self.res
        
    def _post_order(self, root):
        if not root:
            return '#'
        s = '{},{},{}'.format(str(root.val), self._post_order(root.left), self._post_order(root.right))
        self.subtrees[s] += 1
        if self.subtrees[s] == 2:
            self.res.append(root)
        return s
