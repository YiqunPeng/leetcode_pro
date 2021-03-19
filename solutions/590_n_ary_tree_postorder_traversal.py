class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        st = [root]
        res = []
        while st:
            node = st.pop()
            res.append(node.val)
            st.extend(node.children)
        return res[::-1]
