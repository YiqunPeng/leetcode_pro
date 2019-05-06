# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode: 
        """Reversed inorder traversal

        Running Time: O(n) where n is the number of nodes in the tree.
        """     
        def inorder(root, s):            
            if root.right:
                s = inorder(root.right, s) 
                
            root.val = s = s + root.val            
            
            if root.left:
                s = inorder(root.left, s)
            
            return s
          
        if not root: return root  
        
        inorder(root, 0)
        return root
