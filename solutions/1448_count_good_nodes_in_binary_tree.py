class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        st = [(root, -10001)]
        while st:
            node, max_v = st.pop()
            if max_v <= node.val:
                res += 1
                max_v = node.val
            if node.left:
                st.append((node.left, max_v))
            if node.right:
                st.append((node.right, max_v))
        return res
