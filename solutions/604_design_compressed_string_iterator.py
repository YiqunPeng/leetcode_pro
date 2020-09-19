class StringIterator:

    def __init__(self, compressedString: str):
        """Queue.

        Running time: O(n) where n is the length of compressedString.
        """
        self.q = collections.deque()
        
        c, n = '', 0
        for i in range(len(compressedString)):
            if compressedString[i].isdigit():
                n = n * 10 + int(compressedString[i])
            else:
                if c:
                    self.q.append([c, n])
                c = compressedString[i]
                n = 0
        if c:
            self.q.append([c, n])
        
    def next(self) -> str:
        """Running time: O(1).
        """
        if not self.hasNext():
            return ' '
        res = self.q[0][0]
        if self.q[0][1] == 1:
            self.q.popleft()
        else:
            self.q[0][1] -= 1
        return res
        

    def hasNext(self) -> bool:
        """Running time: O(1).
        """
        return self.q