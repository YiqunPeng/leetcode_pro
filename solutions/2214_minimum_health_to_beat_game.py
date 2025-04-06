class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        d_sum, d_max = 0, 0
        for i in range(len(damage)):
            d_sum += damage[i]
            d_max = max(d_max, damage[i])
        return d_sum - min(d_max, armor) + 1