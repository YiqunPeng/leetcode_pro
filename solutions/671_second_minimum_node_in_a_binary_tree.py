class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left:
            return -1
        l = root.left.val
        r = root.right.val
        if l == root.val:
            l = self.findSecondMinimumValue(root.left)
        if r == root.val:
            r = self.findSecondMinimumValue(root.right)
        if l != -1 and r != -1:
            return min(l, r)
        return l if l != -1 else r
