class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """Array.

        Running time: O(n) where n is the number of items in mat.
        """
        p = [0] * len(mat)
        for j in range(len(mat[0])):
            for i in range(1, len(mat)):
                while mat[i][p[i]] < mat[0][j]:
                    p[i] += 1
                if mat[i][p[i]] != mat[0][j]:
                    break
            else:
                return mat[0][j]
        
        return -1