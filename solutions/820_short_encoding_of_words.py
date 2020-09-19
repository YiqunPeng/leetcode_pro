class TreeNode:
    def __init__(self, val):
        self.v = val
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TreeNode("")
    
    def add(self, word):
        new = False
        node = self.root
        for c in word[::-1]:
            if c not in node.children:
                new = True
                node.children[c] = TreeNode(c)
            node = node.children[c]
        return new

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """Trie.

        Running time: O(k) where k is total number of letters.
        """
        words.sort(key=lambda x: len(x), reverse=True)
        trie = Trie()
        res = 0
        for word in words:
            if trie.add(word):
                res = res + len(word) + 1
        return res
