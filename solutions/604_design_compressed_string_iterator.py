class StringIterator:

    def __init__(self, compressedString: str):
        self.s = list(compressedString[::-1])
        self.c = ''
        self.v = 0
        
        self._populate_letter()


    def next(self) -> str:
        if self.hasNext():
            self.v -= 1
            res = self.c
            if self.v == 0:
                self._populate_letter()
            return res
        return ' '
        

    def hasNext(self) -> bool:
        return self.v > 0


    def _populate_letter(self):
        if self.s:
            self.c = self.s.pop()
        while self.s and '0' <= self.s[-1] <= '9':
            self.v = self.v * 10 + int(self.s.pop())