class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.

        Running time: O(1).
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True    

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.

        Running time: O(1).
        """
        if val not in self.d:
            return False
        p = self.d[val]
        la = self.l[-1]
        self.l[p], self.l[-1] = self.l[-1], self.l[p]
        self.d[la] = p
        self.d.pop(val)
        self.l.pop()
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.

        Running time: O(1).
        """
        return random.choice(self.l)
