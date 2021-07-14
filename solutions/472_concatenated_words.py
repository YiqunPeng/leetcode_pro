class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """DP.
        """
        dp_map = defaultdict(list)
        words = set(words)
        for word in words:
            for i in range(len(word)):
                if i != len(word) - 1 and word[:i+1] in words:
                    dp_map[word].append(i)
                    continue
                for j in dp_map[word]:
                    if word[j+1:i+1] in words:
                        dp_map[word].append(i)
                        break
        res = []
        for k, v in dp_map.items():
            if len(v) >= 1 and v[-1] == len(k) - 1:
                res.append(k)
        return res
