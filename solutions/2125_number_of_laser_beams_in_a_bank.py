class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for row in bank:
            s = row.count('1')
            if s > 0:
                devices.append(s)
        res = 0
        for i in range(1, len(devices)):
            res += devices[i] * devices[i-1]
        return res