# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Stack.

        Running time: O(h) where h is the height of the tree.
        """
        st = []
        res = []
        while st or root:
            if root:
                st.append(root)
                res.append(root.val)
                root = root.left
            else:
                root = st.pop()
                root = root.right
        return res
