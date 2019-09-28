class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [0] * 1000001
        

    def add(self, key: int) -> None:
        """Running time: O(1)
        """
        self.set[key] = 1
        

    def remove(self, key: int) -> None:
        """Running time: O(1)
        """
        self.set[key] = 0
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element

        Running time: O(1)
        """
        return self.set[key]        
