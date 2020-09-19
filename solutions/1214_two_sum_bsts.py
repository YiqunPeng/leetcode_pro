class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """BST.

        Running time: O(mlogn) where m is the number of nodes in root1 
                      and n is the number of nodes in root2.
        """
        def search_bst(t, node):
            if not node:
                return False
            if node.val == t:
                return True
            elif node.val < t:
                return search_bst(t, node.right)
            else:
                return search_bst(t, node.left)
            
            if not root1 or not root2:
                return False
            
        s = [root1]
        while s:
            node = s.pop()
            if not node:
                continue
            s.append(node.left)
            s.append(node.right)

            if search_bst(target - node.val, root2):
                return True

        return False
