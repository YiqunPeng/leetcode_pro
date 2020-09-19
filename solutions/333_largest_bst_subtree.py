class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        """Tree postorder traversal.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        def postorder(node):
            if not node:
                return True, 0, None, None
            if not node.left and not node.right:
                return True, 1, node.val, node.val
            
            lbst, ln, lmin, lmax = postorder(node.left)
            rbst, rn, rmin, rmax = postorder(node.right)
            
            if (not lbst or not rbst) or (lmax and node.val <= lmax) or (rmin and node.val >= rmin):
                return False, max(ln, rn), None, None
            else:
                tmin = lmin if lmin else node.val
                tmax = rmax if rmax else node.val
                return True, ln + rn + 1, tmin, tmax
            
        return postorder(root)[1]
