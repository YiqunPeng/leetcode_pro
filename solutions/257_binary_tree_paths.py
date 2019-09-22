# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """DFS.
        
        Running time: O(n) where n is the number of tree nodes.
        """
        def dfs(node, path, paths):        
            path = str(node.val) if not path else path + '->' + str(node.val)
            
            if not node.left and not node.right:
                paths.append(path)
            else:  
                if node.left:             
                    paths = dfs(node.left, path, paths)
                if node.right:
                    paths = dfs(node.right, path, paths)
                    
            return paths
                
        return dfs(root, '', []) if root else []
            