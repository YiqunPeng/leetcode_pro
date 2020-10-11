class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
    	"""Hash table.

    	Running time: O(m * n) where m and n are the size of picture.
    	"""
        m, n = len(picture), len(picture[0])
        col = [0] * n
        rmap = collections.defaultdict(int)
        for i in range(m):
            row = 0
            for j in range(n):
                if picture[i][j] == 'B':
                    row += 1
                    col[j] += 1
            if row == N:
                h = tuple(picture[i])
                rmap[h] += 1
        res = 0
        for k, v in rmap.items():
            if v == N:
                for j in range(n):
                    if k[j] == 'B' and col[j] == N:
                        res += N
        return res
