class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """Hash set.

        Running time: O(n) where n == len(path).
        """
        seen = set([(0, 0)])
        x, y = 0, 0
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
