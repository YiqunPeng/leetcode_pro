class TrieNode:
    def __init__(self):
        self.children = {}
        self.ending = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.ending = True


class Solution:
    
    def __init__(self):
        self.res = []
        self.trie = Trie()
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.trie.add_word(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                node = self.trie.root
                if board[i][j] in node.children:
                    self._dfs(board, node, i, j, '')
        return self.res
    
    def _dfs(self, board, node, i, j, word):
        c = board[i][j]
        if node.children[c].ending:
            self.res.append(word + c)
            node.children[c].ending = False
        board[i][j] = '#'
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                if board[ni][nj] in node.children[c].children:
                    self._dfs(board, node.children[c], ni, nj, word + c)
        board[i][j] = c
