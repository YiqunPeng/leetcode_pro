class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self._build(preorder[::-1], float('inf'))
    
    def _build(self, arr, bound):
        if not arr or arr[-1] > bound:
            return None
        node = TreeNode(arr.pop())
        node.left = self._build(arr, node.val)
        node.right = self._build(arr, bound)
        return node
