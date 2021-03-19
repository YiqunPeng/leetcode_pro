class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return res
