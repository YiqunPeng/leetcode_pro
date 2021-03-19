class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        lvl = [root]
        while lvl:
            res.append(lvl[-1].val)
            nlvl = []
            for node in lvl:
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
            lvl = nlvl
        return res
