class LogSystem:

    def __init__(self):
        """Design.
        """
        self.d = {}
        self.g = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, id: int, timestamp: str) -> None:
        self.d[timestamp] = id
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.g[granularity]
        s, e = start[:idx], end[:idx]
        res = []
        for k, v in self.d.items():
            if s <= k[:idx] <= e:
                res.append(v)
        return res
