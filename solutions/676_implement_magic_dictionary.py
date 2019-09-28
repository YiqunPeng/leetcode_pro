class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words

        Running time: O(n) where n is the total characters in dict.
        """
        for word in dict:
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c != word[i]:
                        w = word[:i] + c + word[i+1:]
                        self.words.add(w)
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        
        Running time: O(1)
        """
        return word in self.words
