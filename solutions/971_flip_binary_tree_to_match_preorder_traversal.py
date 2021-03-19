class Solution:
    
    def __init__(self):
        self.res = []
        self.p = 0
    
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self._traverse(root, voyage)
        return self.res if self.p == len(voyage) else [-1]
    
    def _traverse(self, root, voyage):
        if not root:
            return
        if root.val != voyage[self.p]:
            self.res = [-1]
            return
        self.p += 1
        if self.p == len(voyage):
            return
        if root.right and root.right.val == voyage[self.p]:
            if root.left:
                self.res.append(root.val)
            self._traverse(root.right, voyage)
            self._traverse(root.left, voyage)
        else:
            self._traverse(root.left, voyage)
            self._traverse(root.right, voyage)
