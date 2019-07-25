#Find the lowest common territory that holds the given two places.
#First column of each row is enclosing region, and following columns
#are all the regions within that row.
class Solution(object):
    
    def scanForGarbage(self, regionName, data):
        for regions in data:
            if(regionName in regions):
                return True
        return False
        
    def recurrse(self, data, region1, region2):
        r1 = None
        r2 = None
        for regions in data:
            if(region1 in regions and region2 in regions):
                return regions[0]
            if(region1 in regions and r1 == None):
                r1 = regions[0]
            if(region2 in regions and r2 == None):
                r2 = regions[0]
        return self.recurrse(data, r1, r2)
            
    def logic(self, data , region1, region2):
        if not(self.scanForGarbage(region1, data)):
            print "Region ", region1, " Not found"
            return
        if not(self.scanForGarbage(region2, data)):
            print "Region ", region2, " Not found"
            return
        print self.recurrse(data, region1, region2)
        
        

#Main
data = [
['America',  'NA'  , 'SA'],
['NA', 'MXC', 'USA', 'CAN'],
['SA', 'Argentina', 'Brazil', 'Chile'],
['MXC', 'Oaxaca', 'Puebla'],
['USA', 'CA', 'WY', 'NY'],
['CAN', 'ON', 'QU', 'SAS']
]
obj = Solution()
obj.logic(data, "CA", "Puebla")
obj.logic(data, "WY", "NY")
obj.logic(data, "Chile", "WY")
obj.logic(data, "gibbrish", "WY")
obj.logic(data, "America", "SAS")

data = [
['Earth', 'South America', 'North America', 'Asia', 'Pacific', 'Africa'],
['Asia', 'China', 'Korea', 'Japan'],
['North America', 'USA', 'Canada'],
['South America', 'Brazil', 'Columbia'],
['Africa', 'Algeria', 'Lybia'],
['China', 'Beijing', 'Shanhai'],
['Japan', 'Tokyo', 'Kyoto'],
['Korea', 'Seoul']
]
obj = Solution()
obj.logic(data, 'Tokyo', 'Kyoto')
obj.logic(data, 'Beijing', 'Japan')
obj.logic(data, 'Seoul', 'Africa')
