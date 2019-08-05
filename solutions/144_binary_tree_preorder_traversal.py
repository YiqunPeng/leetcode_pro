# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Stack.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        stack = []
        preorder = []
        
        while stack or root:
            if root:
                preorder.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        
        return preorder
