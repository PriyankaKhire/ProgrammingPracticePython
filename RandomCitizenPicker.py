# Given a map with cities and their population,
# design an algorithm such that you pick a random citizen from those cities such that
# the probability of picking a citizen from a city is proportional to its population.
from __future__ import division
import random

class NumberLine(object):
    def __init__(self, city, fraction):
        self.city = city
        self.fraction = fraction
        self.range = []

class Approch1(object):
    def __init__(self, m):
        self.map = m
        self.numberLine = []

    def drawOnNumberLine(self):
        #total up the entire population of all the cities
        totalPopulation = 0
        for key in self.map:
            totalPopulation = totalPopulation + self.map[key]
        #Now take the total population and divide each citie's population with total population
        #and since we need to draw this on number line we'd need to srot the array
        #for this purpose we make it into objects so sorting by fracion would be easy
        for key in self.map:
            fraction = self.map[key]/totalPopulation
            nl = NumberLine(key, fraction)
            self.numberLine.append(nl)
        #Now sort those objects so we have a range for each city
        self.numberLine.sort(key=lambda x:x.fraction, reverse=True)
        #Now we fill the range of each city on number line
        previous = 0
        print "The number line is "
        for city in self.numberLine:
            city.range = [previous, previous+city.fraction]
            print city.city, " in range ", city.range
            previous = previous+city.fraction

    def pickCitizen(self):
        #generate number Line
        self.drawOnNumberLine()
        #Pick a random citizen
        citizen = float("%.2f" % random.uniform(0, 1)) 
        #find what city does he belong to
        print "The Lucky citizen is citizen number ", citizen, " from ",
        for city in self.numberLine:
            if(citizen >= city.range[0] and citizen <= city.range[1]):
                print city.city
                return



#Main
m = { 'San Fransisco': 10000000,
      'Los Angeles': 2000000,
      'Seattle': 8000000}
o = Approch1(m)
o.pickCitizen()
