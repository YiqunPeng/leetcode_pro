class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """Array.

        Running time: O(n) where n is the length of distance.
        """
        return min(self._travel(distance, start, destination), self._travel(distance, destination, start))

    def _travel(self, distance, s, d):
        dis = 0
        n = len(distance)
        while s % n != d:
            dis += distance[s % n]
            s += 1
        return dis