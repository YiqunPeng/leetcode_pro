class TrieNode:
    def __init__(self, v):
        self.v = v
        self.children = {}


class FileSystem:

    def __init__(self):
        self.root = TrieNode('')
        

    def createPath(self, path: str, value: int) -> bool:
        """Trie.

        Running time: O(h) where h is the height of the tree.
        """
        dirs = path.split('/')[1:]
        node = self.root
        for i in range(len(dirs)-1):
            if dirs[i] not in node.children:
                return False
            node = node.children[dirs[i]]
        if dirs[-1] in node.children:
            return False
        else:
            node.children[dirs[-1]] = TrieNode(value)
            return True
        
    def get(self, path: str) -> int:
        """Trie.

        Running time: O(h) where h is the height of the tree.
        """
        dirs = path.split('/')[1:]
        node = self.root
        for d in dirs:
            if d not in node.children:
                return -1
            node = node.children[d]
        return node.v
