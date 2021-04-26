class Solution:
    
    def __init__(self):
        self.res = []
        self.graph = defaultdict(list)
        self.n = 0
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for f, t in tickets:
            self.graph[f].append(t)
        for k in self.graph:
            self.graph[k].sort()
        self.n = len(tickets) + 1
        self._dfs('JFK')
        return self.res
    
    def _dfs(self, from_city):
        self.res.append(from_city)
        if len(self.res) == self.n:
            return True
        to_cities = self.graph[from_city]
        for i in range(len(self.graph[from_city])):
            to_city = self.graph[from_city][i]
            self.graph[from_city] = to_cities[:i] + to_cities[i+1:]
            if self._dfs(to_city):
                return True
            self.graph[from_city] = to_cities
        self.res.pop()
        return False
