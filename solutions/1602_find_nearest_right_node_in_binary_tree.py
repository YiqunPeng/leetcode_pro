class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        lvl = [root]
        while lvl:
            nlvl = []
            for i in range(len(lvl)):
                if lvl[i] == u:
                    return lvl[i+1] if i < len(lvl) - 1 else None
                if lvl[i].left:
                    nlvl.append(lvl[i].left)
                if lvl[i].right:
                    nlvl.append(lvl[i].right)
            lvl = nlvl
