class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        start = 1
        n = 0
        while candies > 0:
            res[n] += min(candies, start)
            candies -= start
            start += 1
            n += 1
            if n == num_people:
                n = 0
        return res
