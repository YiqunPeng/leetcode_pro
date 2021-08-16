class TreeNode:
    
    def __init__(self, val=''):
        self.val = val
        self.children = defaultdict(TreeNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True
        
    def search(self, word: str) -> bool:
        return self._dfs(word, self.root)
        
    def _dfs(self, word, node):
        if not word:
            return node.end
        if word[0] == '.':
            return any(self._dfs(word[1:], child) for child in node.children.values())
        else:
            return word[0] in node.children and self._dfs(word[1:], node.children[word[0]])
