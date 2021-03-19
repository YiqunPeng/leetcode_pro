class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = collections.defaultdict(list)
        self.f = collections.defaultdict(set)
        self.n = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.t[userId].append((-self.n, tweetId))
        self.n += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = self.f[userId] | set([userId])
        h = []
        for u in users:
            h.extend(self.t[u][:])
        heapq.heapify(h)
        res = []
        for i in range(min(10, len(h))):
            n, tid = heapq.heappop(h)
            res.append(tid)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.f[followerId].discard(followeeId)