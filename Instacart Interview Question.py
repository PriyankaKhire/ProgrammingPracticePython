'''
Given an input of cards that have suits { +, -, = },
values { A, B, C }, and different counts of values [1 - 3]. Find a valid hand.
A valid hand consists of 3 cards.
Where all the suits are different or the same, all the values are different or the same,
and all counts are different or the same.

Example 1.

Given cards: { +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA }

Valid hands are:
{ +AA, +AA, +AA }

[+, +, +] suit is the same
[A, A, A] value is the same
[2, 2, 2] count is the same

{ -A, -AA, -AAA }

[-, -, -] suit is the same
[A, A, A] value is the same
[1, 2, 3] count is the different

{-C, -B, -A }

[-, -, -] suit is the same
[C, B, A] value is different
[1, 1, 1] count is the same

{ +AA, -AA, =AA }

[+, -, =] suit is the different
[A, A, A] value is same
[2, 2, 2] count is the same

Example 2.

The following hand is also valid { -A, +BB, =CCC }

[+, -, =] suit is different
[A, B, C] value is different
[1, 2, 3] count is different

Task

Write a program to return any first valid hand in the given list of cards from stdin.

+AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA

Output any valid hand.
'''
class isValid(object):
    def countOfCard(self, hand):
        # all counts are different or the same
        if (((len(hand[0]) == len(hand[1]))and (len(hand[1]) == len(hand[2])) and (len(hand[2]) == len(hand[0]))) or ((len(hand[0]) != len(hand[1])) and (len(hand[1]) != len(hand[2])) and (len(hand[2]) != len(hand[0])))):
            return True
        return False

    def suitsOfCards(self, hand):
        # all the suits are different or the same
        suits = [list(card)[0] for card in hand]
        if((suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[0]) or (suits[0] != suits[1] and suits[1] != suits[2] and suits[2] != suits[0]) ):
            return True
        return False

    def valueOfCards(self, hand):
        # all the values are different or the same
        value = [list(card)[1] for card in hand]
        if((value[0] == value[1] and value[1] == value[2] and value[2] == value[0]) or (value[0] != value[1] and value[1] != value[2] and value[2] != value[0]) ):
            return True
        return False

    def logic(self, hand):
        if(self.countOfCard(hand) and self.suitsOfCards(hand) and self.valueOfCards(hand)):
            return True
        return False
    
# recursive approach
class Soluiton1(object):
    def logic(self, cards, visited, combinaiton, finalAnswer):
        isValidObj =isValid()
        if (len(combinaiton) == 3 and isValidObj.logic(combinaiton)):
            if (sorted(combinaiton) not in finalAnswer):
                finalAnswer.append(sorted(combinaiton))
            return
        for i in range(len(cards)):
            if(visited[i] == False):
                visited[i] = True
                self.logic(cards, visited, combinaiton+[cards[i]], finalAnswer)
                visited[i] = False
    
    def generateHand(self, cards):
        finalAnswer = []
        self.logic(cards, [False for i in range(len(cards))], [], finalAnswer)
        for ans in finalAnswer:
            print ans

# O(n^3)
class Solution2(object):
    def generateHand(self, cards):
        finalAnswer = []
        isValidObj =isValid()
        for i in range(len(cards)):
            #print "ith card", cards[i],
            for j in range(i+1, len(cards)):
                #print "jth card", cards[j],
                for k in range(j+1, len(cards)):
                    #print "kth card", cards[k]
                    combination = [cards[i], cards[j], cards[k]]
                    if(isValidObj.logic(combination)):
                        if (sorted(combination) not in finalAnswer):
                            finalAnswer.append(sorted(combination))
        print finalAnswer
                    

# Main 1
cards = ['+AA', '-AA', '+AA', '-C', '-B', '+AA', '-AAA', '-A', '=AA']
obj = Soluiton1()
#obj.generateHand(cards)

obj = Solution2()
obj.generateHand(cards)
        
