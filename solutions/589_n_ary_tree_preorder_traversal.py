class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        st = [root]
        while st:
            node = st.pop()
            res.append(node.val)
            st.extend(node.children[::-1])
        return res
