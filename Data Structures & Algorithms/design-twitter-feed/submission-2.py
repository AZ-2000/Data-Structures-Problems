import heapq

class Twitter:
    def __init__(self):
        self.user_tweet = defaultdict(set)
        self.follow_map = defaultdict(set)
        self.timestamp = 0
        self.tweet_count = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId].add(tweetId)
        self.tweet_count[userId].append((self.timestamp, userId, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_list = list(self.tweet_count[userId])
        print(userId, self.tweet_count[userId])
        for followee_Id in self.follow_map[userId]:
            tweet_list.extend(self.tweet_count[followee_Id])
        heapq.heapify(tweet_list)
        while len(tweet_list) > 10:
            heapq.heappop(tweet_list)
        heapq.heapify_max(tweet_list)
        news_feed = []
        heapq.heapify_max(tweet_list)

        news_feed = []

        while tweet_list and len(news_feed) < 10:
            tweet = heapq.heappop_max(tweet_list)
            news_feed.append(tweet[2])
        return news_feed



    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
