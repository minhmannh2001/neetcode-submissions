from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        # userId → list of (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # userId → set of followeeId
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # gom tweet của mình + tất cả người mình follow
        all_tweets = list(self.tweets[userId])
        for followeeId in self.follows[userId]:
            all_tweets += self.tweets[followeeId]

        # sort theo timestamp giảm dần → lấy 10 đầu
        all_tweets.sort(key=lambda x: -x[0])
        return [tweetId for (_, tweetId) in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)