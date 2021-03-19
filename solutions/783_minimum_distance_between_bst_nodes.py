class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = None
        st = []
        res = float('inf')
        while root or st:
            if root:
                while root:
                    st.append(root)
                    root = root.left
            else:
                root = st.pop()
                if prev is not None:
                    res = min(res, root.val - prev)
                prev = root.val
                root = root.right
        return res
