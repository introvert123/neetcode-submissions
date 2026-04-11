class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set) #the reason why we are using a set is bcoz operations take O(1) time
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count = self.count - 1
        self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        self.followMap[userId].add(userId)

        # we are just pushing the latest tweet of every followee + user
        # now the heap size is no. of followees + user
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1 
                count, tweetId = self.tweetMap[followee][idx]
                heap.append((count, tweetId, followee, idx - 1))

        heapq.heapify(heap)
        
        #Pop the most recent tweet from heap, now push the next older tweet from that same user.
        while heap and len(res) < 10:
            count, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[followee][idx] #next recent tweet from same user
                heapq.heappush(heap, (count, tweetId, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
