class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        """String.

        Running time: O(n) where n is the length of dictionary.
        """
        self.dictionary = set(dictionary)
        
        self.abbrs = collections.defaultdict(int)
        for word in self.dictionary:
            abbr = self.get_abbr(word)
            self.abbrs[abbr] += 1
                
    def get_abbr(self, word: str) -> str:
        """Running time: O(1).
        """
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
        
    def isUnique(self, word: str) -> bool:
        """Running time: O(1).
        """
        abbr = self.get_abbr(word)  
        if word in self.dictionary:
            return self.abbrs[abbr] == 1
        else:
            return self.abbrs[abbr] == 0