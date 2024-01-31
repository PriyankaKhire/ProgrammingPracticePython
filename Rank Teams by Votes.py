# Rank Teams by Votes
# https://leetcode.com/problems/rank-teams-by-votes/description/
class Solution(object):
    def getRank(self, votes):
        # Where key = rank 1 to N, Value = {team Id: count}
        rank = {}
        for voter in votes:
            for i in range(len(voter)):
                if (i not in rank):
                    rank[i] = {}
                if (voter[i] not in rank[i]):
                    rank[i][voter[i]] = 0
                rank[i][voter[i]] += 1
        return rank
    
    def tieBreaker(self, rank, tiesList, teamRank):
        print "Entering tie breaker"
        for r in range(teamRank+1, len(rank)):
            print "rank",r, "Ties list", tiesList
            if (len(tiesList) <= 1):
                break
            highScore = 0
            highScoredTeams = []
            # what votes did teams scored in this rank
            for team in tiesList:
                # if team didn't show up in this place
                if (team[0] not in rank[r]):
                    continue
                # if this team scored less than other teams
                if (highScore > rank[r][team[0]]):
                    continue
                # update the high score
                highScore = rank[r][team[0]]
                # add to highscoring teams
                highScoredTeams.append(team)
            # copy highScoring teams to tiesList (this is just like recursion)
            tiesList = highScoredTeams[:]





    
    def sortRank(self, rank):
        output = ""
        for r in rank:
            print r
            ties = []
            highScore = 0
            for teamScore in reversed(sorted(rank[r].items(), key=lambda x: x[1])):
                if (teamScore[1] < highScore):
                    # we no longer wish to see rest of the team scores since the array is sorted in descending order
                    break
                # this is truly just for the first team with highest score
                highScore = max(highScore, teamScore[1])
                ties.append(teamScore)
            # Call tie breaker
            self.tieBreaker(rank, ties, r)
            

    def rankTeams(self, votes):
        rank = self.getRank(votes)
        self.sortRank(rank)
        """
        :type votes: List[str]
        :rtype: str
        """
        