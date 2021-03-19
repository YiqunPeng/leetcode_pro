class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        st1, st2 = [], []
        res = []
        self._push_left(st1, root1)
        self._push_left(st2, root2)
        while st1 or st2:
            if not st2 or (st1 and st1[-1].val < st2[-1].val):
                s = st1
            else:
                s = st2
            n = s.pop()
            res.append(n.val)
            self._push_left(s, n.right)
        return res
    
    def _push_left(self, st, node):
        while node:
            st.append(node)
            node = node.left
