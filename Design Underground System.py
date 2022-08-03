# Design Underground System
# https://leetcode.com/problems/design-underground-system/
class Station(object):
    def __init__(self, startStation, t):
        self.stationName = startStation
        self.t = t
        
class UndergroundSystem(object):

    def __init__(self):
        # key = id val = Station(startStation, t)
        self.customerData = {}
        # key = startStation-endStation val = [t1, t2...]
        self.stationTravelTimes = {}
        

    def checkIn(self, id, stationName, t):
        self.customerData[id] = Station(stationName, t)
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
    
    def checkOut(self, id, stationName, t):
        # create station name
        stationNames = self.customerData[id].stationName +'-'+ stationName
        # calculate travel time
        travelTime = t - self.customerData[id].t
        # delete the customer data we do this so if same customer travels again we have fresh travel times
        del self.customerData[id]
        # insert Station names and travel times into hash
        if (stationNames not in self.stationTravelTimes):
            self.stationTravelTimes[stationNames] = []
        self.stationTravelTimes[stationNames].append(travelTime)
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def getAverageTime(self, startStation, endStation):
        return (sum(self.stationTravelTimes[startStation+'-'+endStation])/float(len(self.stationTravelTimes[startStation+'-'+endStation])))
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
