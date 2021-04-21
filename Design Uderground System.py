# Design Underground System
# https://leetcode.com/problems/design-underground-system/
class Traveller(object):
    def __init__(self, id, startStation, t):
        self.id = id
        self.startStation = startStation
        self.checkinTime = t

class Station(object):
    def __init__(self, name):
        self.name = name
        # key = station name val = [travel times]
        self.endStations = {}
    
    def addStation(self, station, travelTime):
        if (station not in self.endStations):
            self.endStations[station] = []
        self.endStations[station].append(travelTime)
    
    def calculateAvg(self, station):
        endTimesArray = self.endStations[station]
        return sum(endTimesArray)/float(len(endTimesArray))
    
class UndergroundSystem(object):

    def __init__(self):
        self.travellers = {}
        self.startStations = {}

    def checkIn(self, id, stationName, t):
        # Create traveller object
        traveller = Traveller(id, stationName, t)
        # add it to hash table.
        self.travellers[id] = traveller
        # if the start station doesnt exist in stations hash
        if (stationName not in self.startStations):
            # create the object
            station = Station(stationName)
            # add it to hash
            self.startStations[stationName] = station
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def checkOut(self, id, stationName, t):
        # get the traveller object
        travellerObj = self.travellers[id]
        # remove key from dict
        del self.travellers[id]
        # get travel time
        travelTime = t - travellerObj.checkinTime
        # get station object
        stationObject = self.startStations[travellerObj.startStation]
        # add the travel time
        stationObject.addStation(stationName, travelTime)
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def getAverageTime(self, startStation, endStation):
        return self.startStations[startStation].calculateAvg(endStation)
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
