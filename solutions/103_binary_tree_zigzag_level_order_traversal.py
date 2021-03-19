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
        lvl = [root]
        res = []
        d = 1
        while lvl:
            values = []
            nlvl = []
            for node in lvl:
                values.append(node.val)
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
            if d % 2 == 1:
                res.append(values)
            else:
                res.append(values[::-1])
            lvl = nlvl
            d += 1
        return res
            