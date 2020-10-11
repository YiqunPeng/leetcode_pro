class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        na = arr[:]
        stable = False
        while not stable:
            stable = True
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    na[i] = arr[i] + 1
                    stable = False
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    na[i] = arr[i] - 1
                    stable = False
                else:
                    na[i] = arr[i]
            arr = na[:]
        return arr
