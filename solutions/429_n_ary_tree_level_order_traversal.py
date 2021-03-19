class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        lvl = [root]
        res.append([n.val for n in lvl])
        while lvl:
            nlvl = []
            for node in lvl:
                for c in node.children:
                    nlvl.append(c)
            lvl = nlvl
            if lvl:
                res.append([n.val for n in lvl])
        return res
