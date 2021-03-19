class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        lvl = [root]
        while lvl:
            nlvl = []
            maxv = lvl[0].val
            for node in lvl:
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
                maxv = max(maxv, node.val)
            res.append(maxv)
            lvl = nlvl
        return res
