class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        """Math.

        Running time: O(n) where n is the number of nuts.
        """
        def get_distance(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])
    
        d = sum(get_distance(tree, nut) for nut in nuts) * 2
        return min(d + get_distance(nut, squirrel) - get_distance(nut, tree) for nut in nuts)            
