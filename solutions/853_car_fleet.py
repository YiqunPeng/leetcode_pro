class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Array.

        Running time: O(klogk) where k is the number of cars.
        """
        if not position:
            return 0
        
        re = {position[i]: (target - position[i]) / speed[i] for i in range(len(position))}
        position.sort(reverse=True)
        
        fleets = 1
        t = re[position[0]]
        for p in position[1:]:
            if t < re[p]:
                fleets += 1
                t = re[p]
        
        return fleets        
        