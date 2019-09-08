class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """Math.

        Running time: O(1)
        """
        v = [p1, p2, p3, p4]
        e = []
        for i, p in enumerate(v):
            for j, q in enumerate(v[i+1:]):
                e.append(((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2, q[0] - p[0], q[1] - p[1]))
        
        e.sort(key=lambda x: x[0])   
        return e[0][0] > 0 and e[-1][0] == e[-2][0] and e[-1][1] * e[-2][1] + e[-1][2] * e[-2][2] == 0
        