class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        minv = abs(root.val - target)
        while root:
            if abs(root.val - target) < minv:
                minv = abs(root.val - target)
                res = root.val
            if root.val == target:
                return res
            elif root.val > target:
                root = root.left
            else:
                root = root.right
        return res
