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
        def insert(node):
            if not node.left and not node.right:
                if node.val > val:
                    node.left = TreeNode(val)
                else:
                    node.right = TreeNode(val)
                return
            
            if node.val > val:
                if node.left:
                    insert(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    insert(node.right)
                else:
                    node.right = TreeNode(val)
            
        
        if not root:
            return TreeNode(val)
        
        insert(root)
        return root