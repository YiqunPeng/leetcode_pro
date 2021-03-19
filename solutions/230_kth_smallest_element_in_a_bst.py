class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        st = []
        while root or st:
            if root:
                while root:
                    st.append(root)
                    root = root.left
            else:
                root = st.pop()
                res.append(root.val)
                if len(res) == k:
                    return res[-1]
                root = root.right
