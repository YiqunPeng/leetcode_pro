class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        self.node = root

    def next(self) -> int:
        while self.node:
            self.st.append(self.node)
            self.node = self.node.left
        self.node = self.st.pop()
        res = self.node.val
        self.node = self.node.right
        return res
        
    def hasNext(self) -> bool:
        return self.st or self.node
