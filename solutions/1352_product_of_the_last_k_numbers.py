class ProductOfNumbers:

    def __init__(self):
        """Prefix array.
        """
        self.pref = [1]

    def add(self, num: int) -> None:
        """Running time: O(1).
        """
        if num == 0:
            self.pref = [1]
        else:
            self.pref.append(self.pref[-1] * num)
        
    def getProduct(self, k: int) -> int:
        """Running time: O(1).
        """
        if k >= len(self.pref):
            return 0
        return self.pref[-1] // self.pref[-k-1]
