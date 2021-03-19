class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        lf = set()
        v = set([id])
        q = deque([(id, 0)])
        while q:
            p, l = q.popleft()
            if l == level:
                lf.add(p)
                continue
            for fri in friends[p]:
                if fri not in v:
                    q.append((fri, l + 1))
                    v.add(fri)
        videos = defaultdict(int)
        for p in lf:
            for vi in watchedVideos[p]:
                videos[vi] += 1
        return [k for k, v in sorted(videos.items(), key=lambda x: (x[1], x[0]))]
