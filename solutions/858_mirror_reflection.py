class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        np = p
        cnt = 0
        while np % q:
            np += p
            cnt += 1
        if np // q % 2 == 0:
            return 2
        elif cnt % 2 == 0:
            return 1
        else:
            return 0
