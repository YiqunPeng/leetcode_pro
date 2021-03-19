class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        st = [(root, 0)]
        while st:
            node, path = st.pop()
            path = path ^ (1 << node.val)
            if not node.left and not node.right:
                if path & (path - 1) == 0:
                    res += 1
            if node.left:
                st.append((node.left, path))
            if node.right:
                st.append((node.right, path))
        return res
