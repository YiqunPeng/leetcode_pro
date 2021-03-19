class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """BFS.

        Running time: O(n) where n is the total number of nodes in the tree.
        """
        lvl = [root]
        while True:
            nlvl = []
            for node in lvl:
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
            if not nlvl:
                return lvl[0].val
            lvl = nlvl
