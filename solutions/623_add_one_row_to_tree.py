class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            nroot = TreeNode(v, root)
            return nroot
        curr_d = 1
        lvl = [root]
        while curr_d != d - 1:
            nlvl = []
            for node in lvl:
                if node.left:
                    nlvl.append(node.left)
                if node.right:
                    nlvl.append(node.right)
            lvl = nlvl
            curr_d += 1
        for node in lvl:
            if node.left:
                l = node.left
                node.left = TreeNode(v, l)
            else:
                node.left = TreeNode(v)
            if node.right:
                r = node.right
                node.right = TreeNode(v, None, r)
            else:
                node.right = TreeNode(v)
        return root
