class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []
        for n, s, e in trips:
            stops.append((s, n, 's'))
            stops.append((e, n, 'e'))
        stops.sort()
        p = 0
        for i in range(len(stops)):
            stop, n, c = stops[i]
            if c == 's':
                p += n
            else:
                p -= n
            if i < len(stops) - 1 and stops[i+1][0] != stop and p > capacity:
                return False
        return True
