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
        def postorder(root):
            if not root.left and not root.right:
                return 1, True

            v, uni = 0, True
            l, luni, r, runi = 0, True, 0, True
            
            if root.left:
                l, luni = postorder(root.left)
                uni = luni and root.left.val == root.val
            
            
            if root.right:
                r, runi = postorder(root.right)
                uni = uni and runi and root.right.val == root.val

            v = l + r
            if uni:
                v += 1
            return v, uni
        
        return postorder(root)[0] if root else 0
