class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr = collections.defaultdict(set)
        for word in dictionary:
            if len(word) <= 2:
                a = word
            else:
                a = word[0] + str(len(word)-2) + word[-1]
            self.abbr[a].add(word)

    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            a = word
        else:
            a = word[0] + str(len(word)-2) + word[-1]
        if a not in self.abbr or self.abbr[a] == set([word]):
            return True
        else:
            return False
