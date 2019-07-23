class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:        
        """DFS

        Running time: O(k) where k is the number of pixels in image.
        """
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == color:
                image[r][c] = newColor
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    dfs(nr, nc)
        
        if not image:
            return image
        
        m, n, color = len(image), len(image[0]), image[sr][sc]
        if color != newColor:
            dfs(sr, sc)
        
        return image
