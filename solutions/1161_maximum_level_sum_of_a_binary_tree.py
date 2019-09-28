# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """BFS.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        lvl = collections.deque([root])
        
        max_v = root.val
        ret, n, l = 1, 1, 2
        
        while lvl:
            s = 0
            
            for i in range(n):
                node = lvl.popleft()
                if node.left:
                    lvl.append(node.left)
                    s += node.left.val
                if node.right:
                    lvl.append(node.right)
                    s += node.right.val

            if max_v < s:
                max_v = s
                ret = l
                
            n = len(lvl)
            l += 1
        
        return ret