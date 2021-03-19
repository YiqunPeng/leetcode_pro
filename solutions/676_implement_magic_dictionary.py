class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def buildDict(self, dictionary: List[str]) -> None:
        """Hash table.

        Running time: O(n) where n == len(dictionary).
        """
        for word in dictionary:
            n = len(word)
            if n not in self.d:
                self.d[n] = set()
            self.d[n].add(word)

    def search(self, searchWord: str) -> bool:
        """Hash table.

        Running time: O(n * k) where n == len(dictionary) and k == len(searchWord).
        """
        n = len(searchWord)
        if n not in self.d:
            return False
        for word in self.d[n]:
            diff = 1
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff -= 1
                    if diff == -1:
                        break
            if diff == 0:
                return True
        return False