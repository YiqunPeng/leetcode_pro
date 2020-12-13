class Solution:
    def nextClosestTime(self, time: str) -> str:
        """String.
        """
        nums = sorted([time[0], time[1], time[3], time[4]])
        for i in nums:
            if i > time[4]:
                return time[:4] + i
        for i in nums:
            if i > time[3] and i <= '5':
                return time[:3] + i + nums[0]
        for i in nums:
            if i > time[1] and (time[0] != '2' or i <= '4'):
                return time[0] + i + ':' + nums[0] * 2
        for i in nums:
            if i > time[0] and i <= '2':
                return i + nums[0] + ':' + nums[0] * 2
        return nums[0] * 2 + ':' + nums[0] * 2
