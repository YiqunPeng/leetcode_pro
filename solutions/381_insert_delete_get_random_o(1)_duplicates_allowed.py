class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.d = defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].append(len(self.l))
        self.l.append([val, len(self.d[val]) - 1])
        return len(self.d[val]) == 1
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.d[val] == list():
            return False
        pos = self.d[val][-1]
        lval, dpos = self.l[-1]
        self.d[lval][dpos] = pos
        self.l[pos] = [lval, dpos]
        self.d[val].pop()
        self.l.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)[0]
