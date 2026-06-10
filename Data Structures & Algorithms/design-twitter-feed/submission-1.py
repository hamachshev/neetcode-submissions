class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.timeline = []
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.timeline, (-self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        nf = self.timeline.copy()
        res = []
        while len(res) < 10 and nf:
            _, tweetUserId, tweetId = heapq.heappop(nf)
            
            if tweetUserId in self.follows[userId] or tweetUserId == userId:
                res.append(tweetId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

        

