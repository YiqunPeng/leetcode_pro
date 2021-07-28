class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """BFS.
        """
        words = set(wordList)
        if endWord not in words:
            return []
        layer = defaultdict(list)
        layer[beginWord] = [[beginWord]]
        while layer:
            nlayer = defaultdict(list)
            for k, v in layer.items():
                if k == endWord:
                    return v
                for i in range(len(k)):
                    for c in string.ascii_lowercase:
                        nk = k[:i] + c + k[i+1:]
                        if nk in words:
                            nlayer[nk].extend(vv + [nk] for vv in v)
            words -= set(nlayer.keys())
            layer = nlayer
        return []
