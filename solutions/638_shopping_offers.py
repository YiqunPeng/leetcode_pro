class Solution:
    
    def __init__(self):
        self.res = float('inf')
        self.price = None
        self.special = None
        self.cache = {}
    
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.price = price
        self.special = special
        self._dfs(needs, 0)
        return self.res
        
    def _dfs(self, needs, total):
        if all(i == 0 for i in needs):
            self.res = min(self.res, total)
            return
        if tuple(needs) in self.cache:
            return self.cache[tuple(needs)]
        for i in range(len(self.special)):
            nneeds = needs[:]
            valid = True
            for j in range(len(self.special[i])-1):
                nneeds[j] -= self.special[i][j]
                if nneeds[j] < 0:
                    valid = False
                    break
            if valid:
                self._dfs(nneeds, total+self.special[i][-1])
        for i in range(len(self.price)):
            total += self.price[i] * needs[i]
        self.res = min(self.res, total)
        self.cache[tuple(needs)] = self.res
