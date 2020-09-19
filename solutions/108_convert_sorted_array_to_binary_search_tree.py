class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """BST.

        Running time: O(n) where n is the length of nums.
        """
        def build(arr):
            if not arr:
                return None
            
            m = len(arr) // 2
            node = TreeNode(arr[m])
            node.left = build(arr[:m])
            node.right = build(arr[m + 1:])
            
            return node
        
        return build(nums)
