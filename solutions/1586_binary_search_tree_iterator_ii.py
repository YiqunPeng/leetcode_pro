class BSTIterator:

    def __init__(self, root: TreeNode):
        self.next_st = []
        self.buffer = []
        self.idx = -1
        self.node = root

    def hasNext(self) -> bool:
        return self.next_st or self.node or self.idx + 1 < len(self.buffer)        

    def next(self) -> int:
        if self.idx + 1 < len(self.buffer):
            self.idx += 1
            return self.buffer[self.idx].val
        while self.node:
            self.next_st.append(self.node)
            self.node = self.node.left
        node = self.next_st.pop()
        self.node = node.right
        self.buffer.append(node)
        self.idx += 1
        return node.val

    def hasPrev(self) -> bool:
        return self.idx > 0

    def prev(self) -> int:
        self.idx -= 1
        return self.buffer[self.idx].val
