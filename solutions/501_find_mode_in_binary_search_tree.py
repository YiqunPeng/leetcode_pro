class Solution:
    
    def __init__(self):
        self.curr_val = None
        self.curr_freq = 0
        self.max_freq = 0
        self.res = []
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.curr_val = root.val
        self._inorder(root)
        return self.res
        
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self._process(root)
        self._inorder(root.right)
        
    def _process(self, root):
        if root.val == self.curr_val:
            self.curr_freq += 1
        else:
            self.curr_freq = 1
            self.curr_val = root.val
        if self.max_freq < self.curr_freq:
            self.max_freq = self.curr_freq
            self.res = [root.val]
        elif self.max_freq == self.curr_freq:
            self.res.append(root.val)
