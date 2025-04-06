from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """BFS
        """
        word = set(wordList)
        if beginWord == endWord or endWord not in word:
            return 0
        
        q = deque([(beginWord, 1)])
        while q:
            w, s = q.popleft()
            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    if c == w[i]:
                        continue
                    new_w = w[:i] + c + w[i+1:]
                    if new_w == endWord:
                        return s + 1
                    if new_w in word:
                        q.append((new_w, s + 1))
                        word.remove(new_w)
        return 0