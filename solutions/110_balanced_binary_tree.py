# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """Postorder traversal.

        Running time: O(h) where h is the height of the tree.
        """
        def get_balanced_and_height(node):
            if not node:
                return True, 0
            
            l_b, l_h = get_balanced_and_height(node.left)
            r_b, r_h = get_balanced_and_height(node.right)
                        
            if not l_b or not r_b or abs(l_h - r_h) > 1:
                return False, -1
            else:
                return True, max(l_h, r_h) + 1
            
        return get_balanced_and_height(root)[0]