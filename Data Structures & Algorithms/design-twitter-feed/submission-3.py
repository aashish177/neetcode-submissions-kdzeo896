class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        arr = self.tweetMap.get(userId, [])
        arr.append([self.count, tweetId])
        self.tweetMap[userId] = arr
        print(self.tweetMap)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followers = self.followMap.get(userId, set()) | {userId}

        for user in followers:
            if user in self.tweetMap:
                res.extend(self.tweetMap[user])

        heapq.heapify(res)  # min-heap, smallest = most recent

        feed = []
        while res and len(feed) < 10:
            feed.append(heapq.heappop(res)[1])  # ✅ pop most recent first

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.followMap.get(followerId, set())
        followers.add(followeeId)
        self.followMap[followerId] = followers

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
