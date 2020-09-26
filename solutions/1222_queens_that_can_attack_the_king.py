class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """Array.

        Running time: O(n) where n is the number of queens.
        """
        ret = [[] for i in range(8)]
        
        kx, ky = king
        
        for x, y in queens:
            if y == ky:
                if x < kx and (not ret[0] or ret[0][0] < x):
                    ret[0] = [x, y]
                elif x > kx and (not ret[1] or ret[1][0] > x):
                    ret[1] = [x, y]
            
            if x == kx:
                if y < ky and (not ret[2] or ret[2][1] < y):
                    ret[2] = [x, y]
                elif y > ky and (not ret[3] or ret[3][1] > y):
                    ret[3] = [x, y]
            
            if y - x == ky - kx:
                if x < kx and (not ret[4] or ret[4][1] < y):
                    ret[4] = [x, y]
                elif x > kx and (not ret[5] or ret[5][1] > y):
                    ret[5] = [x, y]
            
            if x + y == kx + ky:
                if y < ky and (not ret[6] or ret[6][0] > x):
                    ret[6] = [x, y]
                if y > ky and (not ret[7] or ret[7][0] < x):
                    ret[7] = [x, y]
                    
        return [i for i in ret if i]
       