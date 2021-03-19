class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        values = []
        st = []
        while st or root:
            if root:
                while root:
                    st.append(root)
                    root = root.left
            else:
                node = st.pop()
                values.append(node.val)
                root = node.right
        l, r = 0, len(values) - 1
        while l < r:
            if values[r] + values[l] == k:
                return True
            elif values[r] + values[l] < k:
                l += 1
            else:
                r -= 1
        return False
