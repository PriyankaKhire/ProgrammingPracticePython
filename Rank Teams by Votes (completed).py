# Rank Teams by Votes
# https://leetcode.com/problems/rank-teams-by-votes/description/

class Solution(object):
    def __init__(self):
        # key = team name, value = tuple
        # this tuple will have number of times each team appeared in each place
        # for example if the vote is ABC then voteCount dic will look like this
        # A: (1,0,0, ord("A")) B: (0,1,0, ord("B")) C:(0,0,1, ord("C"))
        # notice the ord(teamName) at the end of each tuple, this is done so we can apply the following rule
        # Rule: If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.
        # Thus ord(teamName) will give the ascii value of teamName and we can use that for ranking.
        self.voteCount = {}
    
    def createTeamTuples(self, votes):
        # get total number of teams
        totalTeams = len(votes[0])
        # get team names
        for v in votes:
            for teamName in v:
                if (teamName not in self.voteCount):
                    # add 0 votes for each position the team can appear in.
                    self.voteCount[teamName] = [0 for i in range(totalTeams)]
                    # add the ord at the end
                    self.voteCount[teamName].append(ord(teamName))
        print "The vote count dic now looks like this", self.voteCount


    # this method doesn't work for following example
    '''
    The vote count dic now looks like this {u'A': [0, 0, 0, 65], u'C': [0, 0, 0, 67], u'B': [0, 0, 0, 66]}
    After counting the votes the dic now looks like this {u'A': [2, 2, 2, 65], u'C': [2, 2, 2, 67], u'B': [2, 2, 2, 66]}
    Final list of tuples looks like this [(2, 2, 2, 65), (2, 2, 2, 67), (2, 2, 2, 66)]
    The list after sorting = [(2, 2, 2, 67), (2, 2, 2, 66), (2, 2, 2, 65)]
    '''
    # to tackle this problem instead of incrementing the vote count, we decrement it.
    def countVotesPositive(self, votes):
        for v in votes:
            for position in range(len(v)):
                teamName = v[position]
                #find the team in voteCount dic, then get the position the team came in this votting session and increment it
                self.voteCount[teamName][position] += 1
        print "After counting the votes the dic now looks like this", self.voteCount
    
    def countVotes(self, votes):
        for v in votes:
            for position in range(len(v)):
                teamName = v[position]
                #find the team in voteCount dic, then get the position the team came in this votting session and increment it
                self.voteCount[teamName][position] -= 1
        print "After counting the votes the dic now looks like this", self.voteCount

    def sortTeamsBasedOnVotes(self):
        # add all the tuples to one list
        finalList = []
        for key in self.voteCount:
            finalList.append(tuple(self.voteCount[key]))
        print "Final list of tuples looks like this", finalList
        # now we sort the final list
        sortedList = sorted(finalList)
        print "The list after sorting =", sortedList
        # gather team names
        output = ""
        for t in sortedList:  
            # chr is opposite of ord
            output += chr(t[-1])
        return output

    def rankTeams(self, votes):
        self.createTeamTuples(votes)
        self.countVotes(votes)
        return self.sortTeamsBasedOnVotes()
        """
        :type votes: List[str]
        :rtype: str
        """
        
