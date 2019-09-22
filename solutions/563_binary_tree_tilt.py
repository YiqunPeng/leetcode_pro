# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """Post order traversal.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        def post_order(node):
            if not node.left and not node.right:
                return 0, node.val
            
            lt, ls, rt, rs = 0, 0, 0, 0
            
            if node.left:
                lt, ls = post_order(node.left)
            if node.right:
                rt, rs = post_order(node.right)
            
            return lt + rt + abs(ls - rs), ls + rs + node.val
    
        return 0 if not root else post_order(root)[0]