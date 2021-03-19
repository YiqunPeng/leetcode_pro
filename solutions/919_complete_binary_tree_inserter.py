class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.leaves = deque(self._get_leaves())

    def insert(self, v: int) -> int:
        front = self.leaves[0]
        if not front.left:
            left = TreeNode(v)
            front.left = left
            self.leaves.append(left)
        elif not front.right:
            right = TreeNode(v)
            front.right = right
            self.leaves.append(right)
            self.leaves.popleft()
        return front.val
                               
    def get_root(self) -> TreeNode:
        return self.root
        
    def _get_leaves(self):
        leaves = []
        lvl = [self.root]
        while lvl:
            nlvl = []
            for node in lvl:
                if not node.left or not node.right:
                    leaves.append(node)
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
            lvl = nlvl
        return leaves
