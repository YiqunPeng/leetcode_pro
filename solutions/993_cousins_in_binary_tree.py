# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """BFS.

        Running time: O(n) where is the number of nodes in the tree.
        """
        from collections import deque
        
        if root.val == x or root.val == y:
            return False
        
        px, dx = None, 0
        py, dy = None, 0
        
        q = deque([(root, 0)])
        while not px or not py:
            node, depth = q.popleft()
            
            if node.left:
                if node.left.val == x:
                    px, dx = node, depth + 1
                elif node.left.val == y:
                    py, dy = node, depth + 1
                q.append([node.left, depth + 1])
            
            if node.right:
                if node.right.val == x:
                    px, dx = node, depth + 1
                elif node.right.val == y:
                    py, dy = node, depth + 1
                q.append([node.right, depth + 1])
        
        if dx == dy and px != py:
            return True
        else:
            return False
   