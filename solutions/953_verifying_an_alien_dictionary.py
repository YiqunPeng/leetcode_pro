class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """Hash table.
        """
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]) or d[words[i][j]] > d[words[i+1][j]]:
                    return False
                if d[words[i][j]] < d[words[i+1][j]]:
                    break
        return True
