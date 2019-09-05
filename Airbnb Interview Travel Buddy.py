# Airbnb interview
# Travel Buddy 
'''
You have a wish list of cities that you would like to travel to.
You are given list of people with their wish lists.
If a person's wish list and your wish list overlaps by 50% or more, then he is your buddy.

Now you need to design an algorithem to recomend cities based on your buddies wish list.
Your are given k which is the max number of cities you can recomend.

Example:

Input:

MyWishList = [a, b, c, d]

People = [
    ['Person1': [a, b, e, f]],
    ['Person2' : [a, c, d, g]],
    ['Person3' : [c, f, e, g]]
    ]

K = 10

Output: [g, e, f]

Explanation:
Person1 has cities a, b common with MyWishList, so the degree of commonality is 2
Person2 has cities a, c, d common with MyWishList, so the degree of commonality is 3
Person3 has cities c common with MyWishList, so the degree of commonality is 1

The question states that "If a person's wish list and your wish list overlaps by 50% or more, then he is your buddy."
So with this rule, Person1 and Person2 are my "Buddies"

Since Person2 has 3 cities in common with MyWishList, they have higher preference than Person1.

The recomended cities would then be the cities that are not in MyWishList but are in my buddies wishlist.
With Person2 it is g
With Person1 it is e, f

Since K = 10 we need to display upto 10 cities, (cannot be more than 10, can be less than 10)
and since Person2 has more in common with MyWishList, their city g has higher preference over
Person1's cities e, f.

So for K = 10
output is [g, e, f]

for K = 2
output is [g, e] or [g, f]

Example:

Input:

MyWishList = [a, b, c, d]

People = {
    ['Person1': [a, b, g, f]],
    ['Person2' : [a, b, c, g]],
    ['Person3' : [c, f, e, g]]
    }

K = 1

Output: [g]

Explanation:
Person2 has a, b, c in common with MyWishList, since overlap is more than 50%, they are qualified to be buddies.
Person1 has a, b in common with MyWishList, since overlap is 50% they are qualified to be buddies.
Person3 has c in common with MyWishList, since overlap is less than 50% they cannot be buddy.

Person2 has city g
Person1 has cities g, f

Since Person2's degree of commonality is 3 they have higher preference over Person1 who's degree of
commonality is 1.

Even though city g is present in both Person1 and Person2's wish lists.
We choose it because it is present in Person with higher degree of commonality.
'''
class Solution(object):
    def __init__(self):
        # key is degree, value is [list of cities]
        self.degreeOfCommonality = {}

    def insertInHash(self, degree, cityList):
        if not(degree in self.degreeOfCommonality):
            self.degreeOfCommonality[degree] = cityList
        else:
            self.degreeOfCommonality[degree] = self.degreeOfCommonality[degree] + cityList

    def findDegreeOfCommonality(self, personWishList, myWishList):
        degree = 0
        for city in personWishList:
            if(city in myWishList):
                degree = degree + 1
        return degree

    def fillDegreeOfCommonalityHash(self, myWishList, People):
        for person in People:
            degree = self.findDegreeOfCommonality(People[person], myWishList)
            # they can be buddies if overlap is 50% or more.
            if(degree >= len(myWishList)/2):
                otherCities = list(set(People[person]) - set(myWishList))
                self.insertInHash(degree, otherCities)
        print "The degree of commonality hash looks like \n",self.degreeOfCommonality

    def addCitiesToOutput(self, cities, output, k):
        for city in cities:
            if(len(output) == k):
                return
            if not(city in output):
                output.append(city)

    def getTopKCities(self, k, output, index, degrees):
        if(len(output) == k or index == len(degrees)):
            print output
            return
        print "The current Degree is",degrees[index]
        cities = self.degreeOfCommonality[degrees[index]]
        print "The cities in this degree are", cities
        # we add only those cities in output that are not present in the output
        print "Output is",output
        self.addCitiesToOutput(cities, output, k)
        print "Output after adding new cities is",output
        self.getTopKCities(k, output, index+1, degrees)
        
        
    def recomendCities(self, myWishList, People, k):
        self.fillDegreeOfCommonalityHash(myWishList, People)
        # reverse=True, coz we want degrees in descending order.
        self.getTopKCities(k, [], 0, sorted(self.degreeOfCommonality, reverse=True))

# Main
myWishList = ['a', 'b', 'c', 'd']
People = {
    'Person1': ['a', 'b', 'e', 'f'],
    'Person2': ['a', 'b', 'd', 'g'],
    'Person3': ['c', 'f', 'e', 'g']
    }
obj = Solution()
obj.recomendCities(myWishList, People, 2)
print "*"*50
myWishList = ['a', 'b', 'c', 'd']
People = {
    'Person1': ['a', 'b', 'g', 'f'],
    'Person2': ['a', 'b', 'c', 'g'],
    'Person3': ['c', 'f', 'e', 'g']
    }
obj = Solution()
obj.recomendCities(myWishList, People, 10)
