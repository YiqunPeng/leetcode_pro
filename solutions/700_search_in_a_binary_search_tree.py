# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """BST.

        Running time: O(h) where h is the height of the tree.
        """
        def search(node):
            if node.val == val:
                return node
            elif node.val > val:
                if node.left:
                    return search(node.left)
                else:
                    return
            else:
                if node.right:
                    return search(node.right)
                else:
                    return
                
        
        if not root:
            return
        
        return search(root)