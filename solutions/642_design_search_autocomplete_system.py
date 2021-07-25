class TrieNode:
    
    def __init__(self):
        self.sentences = defaultdict(int)
        self.children = defaultdict(TrieNode)

        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, sentence, time):
        node = self.root
        for c in sentence:
            node = node.children[c]
            node.sentences[sentence] += time
            
    def search(self, node):
        tuples = [(v, k) for k, v in node.sentences.items()]
        tuples.sort(key=lambda x: (-x[0], x[1]))
        return [k for v, k in tuples[:3]]
        
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.node = self.trie.root
        for i in range(len(sentences)):
            self.trie.add(sentences[i], times[i])
        self.type = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.add(self.type, 1)
            self.type = ''
            self.node = self.trie.root
            return []
        self.node = self.node.children[c]
        self.type += c
        res = self.trie.search(self.node)
        return res
