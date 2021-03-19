# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """BST.

        Running time: O(h) where h is the height of the tree.
        """
        if not root:
            return TreeNode(val)
        self._insert(root, val)
        return root
    
    def _insert(self, root, val):
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self._insert(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self._insert(root.right, val)