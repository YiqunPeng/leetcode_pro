class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """Stack.
        """
        res = [0] * n
        prev = 0
        st = []
        for log in logs:
            fid, op, time = log.split(':')
            fid, time = int(fid), int(time)
            if op == 'start':
                if st:
                    res[st[-1]] += time - prev
                st.append(fid)
                prev = time
            else:
                res[st.pop()] += time - prev + 1
                prev = time + 1
        return res
