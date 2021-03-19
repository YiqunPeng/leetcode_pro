class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if not root:
            return res
        lvl = [root]
        while lvl:
            s = 0
            nlvl = []
            for n in lvl:
                s += n.val
                if n.left:
                    nlvl.append(n.left)
                if n.right:
                    nlvl.append(n.right)
            res.append(s / len(lvl))
            lvl = nlvl
        return res
