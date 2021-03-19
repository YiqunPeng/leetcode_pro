class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = set([start])
        while q:
            pos = q.popleft()
            if arr[pos] == 0:
                return True
            forward = pos + arr[pos]
            backward = pos - arr[pos]
            if forward < len(arr) and forward not in seen:
                seen.add(forward)
                q.append(forward)
            if 0 <= backward and backward not in seen:
                seen.add(backward)
                q.append(backward)
        return False
