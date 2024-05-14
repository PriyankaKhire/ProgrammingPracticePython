# Paying Wages Gusto Interview Question
'''
Given an amount of money to distribute, a list of recipients and how much money each is owed, you should return the list of recipients and how much each would be paid after following the business logic below:  
1. no recipient is paid more than they are owed
2. the amount is divided as evenly as possible between the recipients  

input: { 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 40 
output: { 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 }  

input: { 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 20 
output: { 'ryan': 5, 'stephanie': 5, 'quentin': 5, 'upeka': 5 }  

input: { 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 21 
output: { 'ryan': 2, 'stephanie': 6, 'quentin': 7, 'upeka': 6 }  

input: { 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 22 
output: { 'ryan': 2, 'stephanie': 7, 'quentin': 7, 'upeka': 6 } 

Hint:
First consider sorting according to ammount owed and then according to alphebetical order of the person's name

Another description

a boss is going to give out bonuses, and the boss hopes to divide them evenly among his subordinates, 
but each employee has a bonus cap, which means that the bonus received cannot exceed their cap. If an employee reaches the cap, the remaining bonus will be 
divided equally among those who have not reached the cap. If the amount cannot be divided evenly when divided equally, the extra money will be distributed in alphabetical order 
of their names. For example, there is a bonus of 1,000 yuan now, and there are five people A, B, C, D, and E. 
Their caps are 100, 150, 200, 500, and 600. Then they will eventually get 100, 150, 200, 275, and 275 (if it is divided evenly, each person should get 200, but A and B's caps are smaller, 
so they can only get 100 and 150 at most, and the extra money will be given to D and E). 
Suppose the bonus is 1001, then D will get 276, because D's alphabetical order is higher than E, so the extra 1 yuan that cannot be divided evenly will be given to D.
'''

class Solution(object):
    def createTup(self, moneyOwedMap):
        tupList = []
        for key in moneyOwedMap:
            # create a tuple list such that (moneyOwed, personName)
            t = (moneyOwedMap[key], key)
            tupList.append(t)
        # Now sort such that we first sort by first moneyOwed and then by person Name
        # for example the sorted list should look like [(1, z), (2, a), (2, b)]
        tupList.sort()
        return tupList
    
    def divideMoney(self, tupList, totalAvailable):
        hashMap = {name:0 for (m,name) in tupList}
        # length of tupList is total number of people that are owed money
        # so if we have $4 and 5 people then we cannot distribute the money equally 
        # in this case first 4 people will get $1 each and last person won't get anything
        while(totalAvailable > len(tupList)):
            print "*"*15
            print tupList
            # divide totalAvailable equally amongst people
            dividedAmount = int(totalAvailable/len(tupList))
            print "divided ammout", dividedAmount
            # we cannot give a person more than they are owed 
            peopleIndex = 0
            while(peopleIndex < len(tupList)):
                (moneyOwed, person) = tupList[peopleIndex]
                print "person",person
                # if assigned ammout to this person is more than they are owed 
                if (dividedAmount >= moneyOwed):
                    # assing them the money owed
                    hashMap[person] = moneyOwed
                    # update total
                    totalAvailable -= moneyOwed
                    print "we are assing them complete money owned", moneyOwed
                    # remove them from tupList since no longer owe them any money
                    tupList.pop(peopleIndex)
                    break
                else:
                    # assing them the money owed
                    hashMap[person] = dividedAmount
                    # update total
                    totalAvailable -= dividedAmount
                    print "we are assign them", dividedAmount
                peopleIndex += 1
        print "Total ammoung left", totalAvailable
        #print hashMap
        peopleIndex = 0
        while(totalAvailable > 0):
            (moneyOwed, person) = tupList[peopleIndex]
            # assing them $1 each
            hashMap[person] += 1
            # reduce the total
            totalAvailable -= 1
            # move on to next person
            peopleIndex += 1
        return hashMap


    def logic(self, moneyOwedMap, totalAvailable):
        if (totalAvailable <= 0):
            print "We cannot pay anyone"
            return
        totalMoneyOwed = sum((moneyOwedMap.values()))
        if (totalMoneyOwed < totalAvailable):
            print moneyOwedMap
            return
        tupList = self.createTup(moneyOwedMap)
        print self.divideMoney(tupList, totalAvailable)
# Main
obj = Solution()
obj.logic({ 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 22)
obj.logic({ 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 21)
obj.logic({ 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 20)
obj.logic({ 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 50)
obj.logic({ 'anna': 2, 'matt': 1, 'kevin': 5 } , 4)