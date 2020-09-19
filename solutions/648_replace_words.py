class TrieNode:
    def __init__(self, c):
        self.char = c
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def add(self, word):
        """Running time: O(n) where n is the length of word.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_end = True
    
    def search(self, word):
        """Running time: O(n) where n is the length of word.
        """
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return word
            elif node.children[word[i]].is_end:
                return word[:i+1]
            else:
                node = node.children[word[i]]
        return word

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        """Trie.
        """
        trie = Trie()
        for word in dict:
            trie.add(word)
            
        words = sentence.split(' ')
        for i in range(len(words)):
            words[i] = trie.search(words[i])
        
        return ' '.join(words)
        