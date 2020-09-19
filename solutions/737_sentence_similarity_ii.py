class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """Union find.

        Running time: O(w + p) where w is the length of words1 and p is the length of pairs.
        """
        def find(w1):
            if f[w1] != w1:
                f[w1] = find(f[w1])
            return f[w1]
        
        def union(w1, w2):
            f[find(w2)] = find(w1)
            
        if len(words1) != len(words2):
            return False
        
        f = {}
        for w1, w2 in pairs:
            if w1 not in f:
                f[w1] = w1
            if w2 not in f:
                f[w2] = w2
            union(w1, w2)
            
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                if (words1[i] not in f or words2[i] not in f) or find(words1[i]) != find(words2[i]):
                    return False

        return True