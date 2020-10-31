class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Array.

        Running time: O(k) where k == len(flowerbed).
        """
        p = 0
        while p < len(flowerbed) and flowerbed[p] == 0:
            p += 1
        if p < len(flowerbed):
            n -= p // 2
        else:
            n -= (p + 1) // 2
        for i in range(p + 1, len(flowerbed)):
            if flowerbed[i] == 1:
                n -= max(0, (i - p - 2) // 2)
                p = i
        if p < len(flowerbed):
            n -= max(0, (len(flowerbed) - p - 1) // 2)
        return n <= 0
