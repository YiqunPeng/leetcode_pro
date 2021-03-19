class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if len(arr) == 1:
            return root and root.val == arr[0] and not root.left and not root.right
        if not root or root.val != arr[0]:
            return False
        return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])
