class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ha = hour / 12 * 360 + minutes / 60 * 30
        ma = minutes / 60 * 360
        d = abs(ha - ma)
        return d if d <= 180 else 360 - d
