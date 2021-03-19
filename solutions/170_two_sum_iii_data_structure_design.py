class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.d[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k in self.d:
            if k * 2 == value:
                if self.d[k] > 1:
                    return True
            elif value - k in self.d:
                return True
        return False
