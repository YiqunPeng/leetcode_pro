class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Stack.
        """
        s = []
        res = []
        for a in asteroids:
            if a > 0:
                s.append(a)
            else:
                e = False
                while s and not e:
                    top = s[-1]
                    if top == -a:
                        s.pop()
                        e = True
                    elif top < -a:
                        s.pop()
                    else:
                        e = True
                if not e:
                    res.append(a)
        return res + s 