# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """BST

        Running time: O(h) where h is the height of the BST.
        """
        def search():
            node, pre = root, None
            while node:
                if node.val == key:
                    return node, pre
                pre = node
                if node.val < key:
                    node = node.right
                else:
                    node = node.left
            return None, None
        
        def delete(node):
            if not node.right:
                return node.left
            r = node.right
            while r.left:
                r = r.left
            r.left = node.left
            return node.right
        
        node, pre = search()
        
        if not node:
            return root
        
        if node == root:
            return delete(root)
        if pre.left == node:
            pre.left = delete(node)
        else:
            pre.right = delete(node)
        return root 