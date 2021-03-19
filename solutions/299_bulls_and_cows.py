class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """String.

        Running time: O(n) where n is the length of secret.
        """
        bulls, cows = 0, 0
        sc, gc = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            sc[secret[i]] = sc.get(secret[i], 0) + 1
            gc[guess[i]] = gc.get(guess[i], 0) + 1
        for k, v in sc.items():
            if k in gc:
                cows += min(v, gc[k])
        return str(bulls) + 'A' + str(cows - bulls) + 'B'
