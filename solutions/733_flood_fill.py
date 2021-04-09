class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor != newColor:
            image[sr][sc] = newColor
            self._dfs(image, sr, sc, newColor, oldColor)
        return image
    
    def _dfs(self, image, i, j, nc, oc):
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < len(image) and 0 <= nj < len(image[0]) and image[ni][nj] == oc:
                image[ni][nj] = nc
                self._dfs(image, ni, nj, nc, oc)
