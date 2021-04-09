class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """BFS.

        Running time: O(n) where n is the number of rooms.
        """
        v = set([0])
        q = deque([0])
        while q:
            room = q.popleft()
            for nxt in rooms[room]:
                if nxt not in v:
                    v.add(nxt)
                    q.append(nxt)
        return len(v) == len(rooms)
            