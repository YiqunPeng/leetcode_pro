class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """Tree.
        """
        l = [root]
        while l:
            nl = []
            for i in l:
                if i.left:
                    nl.append(i.left)
                if i.right:
                    nl.append(i.right)
            if not nl:
                return sum([i.val for i in l])
            l = nl
