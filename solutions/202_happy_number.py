class Solution:
    def isHappy(self, n: int) -> bool:
        """Hash set.
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            nn = 0
            while n:
                r = n % 10
                nn += r * r
                n //= 10
            n = nn
            if n == 1:
                return True
        return False
