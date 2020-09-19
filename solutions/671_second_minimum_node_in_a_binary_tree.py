# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """Recursion.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        def find_min(root, val):
            if not root:
                return sys.maxsize
            if root.val > val:
                return root.val
            
            return min(find_min(root.left, val), find_min(root.right, val))
            
        
        l, r = find_min(root.left, root.val), find_min(root.right, root.val)
        
        if min(l, r) != sys.maxsize:
            return min(l, r)
        else:
            return -1
 