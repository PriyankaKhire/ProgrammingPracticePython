# Design A Leaderboard
# https://leetcode.com/problems/design-a-leaderboard/

import heapq
class Leaderboard(object):
    def __init__(self):
        # key = player Id, val = score
        self.scoreBoard = {}

    def addScore(self, playerId, score):
        if (playerId not in self.scoreBoard):
            self.scoreBoard[playerId] = 0
        self.scoreBoard[playerId] += score
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        

    def top(self, K):
        heap = []
        # get all scores
        scores = [self.scoreBoard[key] for key in self.scoreBoard]
        # add k scores to heap
        for i in range(K):
            heapq.heappush(heap, scores[i])
        # maintain min heap of k elements and add rest of the elements
        i = K
        while i < len(scores):
            # add element to heap
            heapq.heappush(heap, scores[i])
            # pop element from heap
            heapq.heappop(heap)
            i = i + 1
        # return sum of top K
        return sum(heap)
        """
        :type K: int
        :rtype: int
        """
        

    def reset(self, playerId):
        self.scoreBoard[playerId] = 0
        """
        :type playerId: int
        :rtype: None
        """
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
