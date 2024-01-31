# Rank Teams by Votes
# https://leetcode.com/problems/rank-teams-by-votes/description/
class TeamVotes(object):
    def __init__(self):
        self.rank = None
        self.count = 0

class Solution(object):
    def display(self, rank, teamNames, reverseTeamNameLookup):
        print teamNames, reverseTeamNameLookup
        for team in rank:
            for teamVote in team:
                print "[",teamVote.rank, teamVote.count,"]",
            print ""

    def fillMatrix(self, votes):
        # matrix where rank[i][j] represents team i with j votes
        rank = []
        # key = team Name val = team number
        team = {}
        # key = team Number val = team Name
        reverseTeamNameLookup = {}
        teamNumber = 0
        for vote in votes:
            for teamName in vote:
                if (teamName not in team):
                    team[teamName] = teamNumber
                    reverseTeamNameLookup[teamNumber] = teamName
                    teamNumber += 1

        # fill matrix with 0 score
        rank = [[TeamVotes() for col in range(len(team))] for row in range(len(team))]
        '''
        The array will look like this for example 1
          1 2 3 
        A
        B
        C
        '''
        # fill the matrix with score
        for i in range(len(votes)):
            for j in range(len(votes[i])):
                teamName = votes[i][j]
                teamNumber = team[teamName]
                #print "teamName", teamName, "teamNumber", teamNumber, "rank", j
                rank[teamNumber][j].count += 1
                rank[teamNumber][j].rank = j
        # return 
        return team, rank, reverseTeamNameLookup
    
    def compareTeams(self, team1, team2):
        # to do complete it

    def tieBreaker(self, teamName, rank):
        # to do complete it
    

    def rankTeams(self, votes):
        team, rank, reverseTeamNameLookup = self.fillMatrix(votes)
        self.display(rank, team, reverseTeamNameLookup)
        self.tieBreaker(reverseTeamNameLookup, rank)
        """
        :type votes: List[str]
        :rtype: str
        """
