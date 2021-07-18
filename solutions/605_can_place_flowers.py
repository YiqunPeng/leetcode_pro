class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Array.

        Running time: O(k) where k == len(flowerbed).
        """
        place = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev = flowerbed[i-1] if i else 0
                nxt = flowerbed[i+1] if i + 1 < len(flowerbed) else 0
                if prev == nxt == 0:
                    place += 1
                    flowerbed[i] = 1
        return place >= n
