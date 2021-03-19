# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """BFS.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        if not root:
            return []
        res = []
        lvl = [root]
        while lvl:
            nlvl = []
            values = []
            for node in lvl:
                values.append(node.val)
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
            lvl = nlvl
            res.append(values)
        return res[::-1]
        