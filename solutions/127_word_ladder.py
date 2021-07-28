class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """BFS.
        """
        words = set(wordList)
        if endWord not in words:
            return 0
        layer = set([beginWord])
        res = 1
        while layer:
            nlayer = set()
            for word in layer:
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        nword = word[:i] + c + word[i+1:]
                        if nword in words:
                            nlayer.add(nword)
            words -= nlayer
            layer = nlayer
            res += 1
        return 0
