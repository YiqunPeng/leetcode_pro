class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.p = self.iter.next() if self.iter.hasNext() else None
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.p

    def next(self):
        """
        :rtype: int
        """
        res = self.p
        self.p = self.iter.next() if self.iter.hasNext() else None
        return res     

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p is not None
