class Solution:

    def __init__(self):
        self.combs = []

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [0] * 10
        self._backtracking(leds, turnedOn, 0)
        return self._gen_time()

    def _backtracking(self, leds, n, idx):
        if n == 0:
            self.combs.append(leds[:])
            return 
        
        for i in range(idx, 10):
            leds[i] = 1
            self._backtracking(leds, n - 1, i + 1)
            leds[i] = 0

    def _gen_time(self):
        res = []
        for c in self.combs:
            hour = 8 * c[0] + 4 * c[1] + 2 * c[2] + 1 * c[3]
            minute = 32 * c[4] + 16 * c[5] + 8 * c[6] + 4 * c[7] + 2 * c[8] + 1 * c[9]
            if 0 <= hour < 12 and 0 <= minute < 60:
                time = str(hour) + ':'
                if 0 <= minute < 10:
                    time += '0'
                time += str(minute)
                res.append(time)
        return res