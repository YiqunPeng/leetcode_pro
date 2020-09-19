class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """String.

        Running time: O(n) where n is the length of secret.
        """
        bulls, cows = 0, 0
        counter = Counter(secret)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                counter[guess[i]] -= 1
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                continue
            if guess[i] in counter and counter[guess[i]] > 0:
                counter[guess[i]] -= 1
                cows += 1
        
        return str(bulls) + 'A' + str(cows) + 'B'