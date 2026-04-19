from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId → [(time, tweetId)]
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # tập hợp user cần lấy tweet (mình + following)
        users = self.follows[userId] | {userId}

        # mỗi user: đẩy tweet MỚI NHẤT vào heap
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1   # index tweet mới nhất
                t, tid = self.tweets[uid][idx]
                # (-time, tweetId, userId, idx_kế_tiếp)
                heapq.heappush(heap, (-t, tid, uid, idx - 1))

        result = []
        while heap and len(result) < 10:
            t, tid, uid, idx = heapq.heappop(heap)
            result.append(tid)

            # còn tweet cũ hơn của user này? push tiếp vào heap
            if idx >= 0:
                t2, tid2 = self.tweets[uid][idx]
                heapq.heappush(heap, (-t2, tid2, uid, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)