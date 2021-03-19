# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """Post order traversal.

        Running time: O(n) where n is the total number of nodes in the tree.
        """
        return self._post_order(root)[0]
    
    def _post_order(self, root):
        if not root:
            return 0, True
        if not root.left and not root.right:
            return 1, True
        res = 0
        lres, luni = self._post_order(root.left)
        rres, runi = self._post_order(root.right)
        uni = False
        v = root.val
        if luni and runi and (not root.right or root.right.val == v) and (not root.left or root.left.val == v):
            uni = True
            res += 1
        return res + lres + rres, uni
