class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """Hash set.

        Running time: O(w + p) where w is the length of words1 and p is the length of pairs.
        """
        if len(words1) != len(words2):
            return False
        
        d = collections.defaultdict(set)
        for w1, w2 in pairs:
            d[w1].add(w2)
            d[w2].add(w1)
            
        for i in range(len(words1)):
            if not (words1[i] == words2[i] or words1[i] in d[words2[i]]):
                return False
            
        return True
