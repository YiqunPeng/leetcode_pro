class Solution:
    
    def __init__(self):
        self.words_parent = {}
    
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        for a, b in pairs:
            self._union(a, b)
        for i in range(len(words1)):
            if self._find(words1[i]) != self._find(words2[i]):
                return False
        return True
    
    def _find(self, w):
        if w not in self.words_parent:
            return w
        if w != self.words_parent[w]:
            self.words_parent[w] = self._find(self.words_parent[w])
        return self.words_parent[w]
    
    def _union(self, a, b):
        if a not in self.words_parent:
            self.words_parent[a] = a
        if b not in self.words_parent:
            self.words_parent[b] = b
        pa = self._find(a)
        pb = self._find(b)
        if pa != pb:
            self.words_parent[pa] = self._find(pb)
