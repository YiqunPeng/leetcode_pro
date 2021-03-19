class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.kt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [timestamp]
        else:
            self.d[key].append(timestamp)
        self.kt[(key, timestamp)] = value 

    def get(self, key: str, timestamp: int) -> str:     
        if timestamp < self.d[key][0]:
            return ''
        idx = min(bisect.bisect_right(self.d[key], timestamp), len(self.d[key]))
        t = self.d[key][idx-1]
        return self.kt[(key, t)]
