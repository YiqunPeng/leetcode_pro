# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        Running time: O(n) where n is the length of nestedList.
        """
        self.s = nestedList[::-1]

    def next(self):
        """
        :rtype: int

        Running time: O(1).
        """
        return self.s.pop().getInteger()
        
        
    def hasNext(self):
        """
        :rtype: bool

        Running time: O(m) where m is the total elements in nestedList.
        """
        while self.s and not self.s[-1].isInteger():
            item = self.s.pop()
            self.s.extend(item.getList()[::-1])
        return self.s
        