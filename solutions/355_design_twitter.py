class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.

        Running time: O(1)
        """
        self.tweets_num = 0
        self.user_tweets = collections.defaultdict(list)
        self.follows = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.

        Running time: O(1)
        """
        self.user_tweets[userId].append((tweetId, self.tweets_num))
        self.tweets_num += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        
        Running time: O(nlogn) where n is the total number of tweets the user's followees have.
        """
        tweets = self.user_tweets[userId][:]
        for user in self.follows[userId]:
            tweets.extend(self.user_tweets[user])
        return [t[0] for t in sorted(tweets, key=lambda x: x[1], reverse=True)[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        
        Running time: O(1)
        """
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        
        Running time: O(1).
        """
        self.follows[followerId].discard(followeeId)
