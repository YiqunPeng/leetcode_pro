class BSTIterator:

    def __init__(self, root: TreeNode):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        node = self.st.pop()
        res = node.val
        node = node.right
        while node:
            self.st.append(node)
            node = node.left
        return res
            
    def hasNext(self) -> bool:
        return self.st
