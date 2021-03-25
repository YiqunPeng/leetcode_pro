class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x = 1
        y = z
        while x <= z and y >= 1:
            v = customfunction.f(x, y)
            if v == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif v < z:
                x += 1
            else:
                y -= 1
        return res
