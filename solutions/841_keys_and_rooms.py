class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """BFS.

        Running time: O(n) where n is the number of rooms.
        """
        v = set([0])
        
        q = collections.deque([0])
        while q:
            r = q.popleft()
            
            for key in rooms[r]:
                if key not in v:
                    q.append(key)
                    v.add(key)
        
        return len(v) == len(rooms)
            