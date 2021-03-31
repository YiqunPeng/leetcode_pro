class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 == 0:
            return self.checkPowersOfThree(n // 3)
        elif (n - 1) % 3 == 0:
            return self.checkPowersOfThree((n - 1) // 3)
        else:
            return False
