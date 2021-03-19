class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """Hash set.
        """
        res = set()
        i = 0
        while x ** i < bound:
            j = 0
            while x ** i + y ** j <= bound:
                res.add(x ** i + y ** j)
                if y == 1:
                    break
                else:
                    j += 1
            if x == 1:
                break
            else:
                i += 1
        return res
