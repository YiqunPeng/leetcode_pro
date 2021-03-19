class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
    	"""Hash table.

    	Running time: O(k) where k is total number of bricks.
    	"""
        d = collections.defaultdict(int)
        for row in wall:
            w = 0
            for b in row[:-1]:
                w += b
                d[w] += 1
        return len(wall) - max(d.values() or [0])
