class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """Hash set.

        Running time: O(w + p) where w is the length of words1 and p is the length of pairs.
        """
        if len(sentence1) != len(sentence2):
            return False
        s = set()
        for a, b in similarPairs:
            s.add((a, b))
            s.add((b, a))
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and (sentence1[i], sentence2[i]) not in s:
                return False
        return True
