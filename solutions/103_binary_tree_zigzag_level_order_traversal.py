# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """BFS.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        if not root:
            return []
        
        r = []
        
        l = [root]
        while l:
            v = [n.val for n in l]
            if len(r) % 2 == 0:
                r.append(v)
            else:
                r.append(v[::-1])
            
            nl = []
            
            for node in l:
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)
            
            l = nl
        
        return r
            