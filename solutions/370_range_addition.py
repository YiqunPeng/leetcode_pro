class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length + 1)
        for s, e, i in updates:
            arr[s] += i
            arr[e+1] -= i
        for i in range(1, length):
            arr[i] += arr[i-1]
        return arr[:-1]
