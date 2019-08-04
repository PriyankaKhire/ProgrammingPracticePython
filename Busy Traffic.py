'''
Given a list of cars traveling from point start to end with speed in the format [start, end, speed]. 
You need to return the list of smallest intervals (segments) 
and the average speed of vehicles in each of those intervals.

Used for road color coding as per traffic prediction used in google maps or lately uber.

Example 1:

Input: [[0, 14, 90], [3, 15, 80]]
Output: [[0, 3, 90], [3, 14, 85], [14, 15, 80]]
Explanation:
car1: [0, 14, 90] car 1 travels from point 0 to 14 with speed 90
car2: [3, 15, 80] car 2 travels from point 3 to 15 with speed 80

Segments:
[0, 3] with average speed 90
[3, 14] speed is (90 + 80) / 2 = 85, where we take the average of all cars here
[14, 15] with average speed is 80
Example 2:

Input = [[5, 15, 20], [10, 20, 30]]
Output = [[5, 10, 20], [10, 15, 25], [15, 20, 30]]
Example 3:

Input: [[5, 15, 20], [10, 20, 30], [7, 25, 10]]
Output: [[5, 7, 20], [7, 10, 15], [10, 15, 20], [15, 20, 20], [20, 25, 10]]
'''
class Solution(object):
	def __init__(self):
		self.hashTable = {}

	def putInHash(self, intervals):
		for interval in intervals:
			if not(interval[0] in self.hashTable):
				self.hashTable[interval[0]] = [interval[2]]
			else:
				self.hashTable[interval[0]].append(interval[2])
			if not(interval[1] in self.hashTable):
				self.hashTable[interval[1]] = [-interval[2]]
			else:
				self.hashTable[interval[1]].append(-interval[2])

	def logic(self):
		speed = 0
		numberOfCars = 0
		intervalTimes = sorted(self.hashTable)
		output = []
		for i in range(len(intervalTimes)):
			if(i > 0):
				print "From interval", intervalTimes[i-1], "to", intervalTimes[i],"the speed was", speed/numberOfCars
				output.append([intervalTimes[i-1], intervalTimes[i], speed/numberOfCars])
			for speeds in self.hashTable[intervalTimes[i]]:
				if(speeds < 0):
					numberOfCars = numberOfCars - 1
				else:
					numberOfCars = numberOfCars + 1
				speed  = speed + speeds
		print output
			

	def intervalSegments(self, intervals):
		self.putInHash(intervals)
		self.logic()

#Main
intervals = [[5, 15, 20], [10, 20, 30], [7, 25, 10], [20, 25, 40]]
obj = Solution()
obj.intervalSegments(intervals)

intervals = [[5, 15, 20], [10, 20, 30]]
obj = Solution()
obj.intervalSegments(intervals)

intervals = [[0, 14, 90], [3, 15, 80]]
obj = Solution()
obj.intervalSegments(intervals)

intervals = [[0,14, 90], [16,20, 70], [3,18,80]]
obj = Solution()
obj.intervalSegments(intervals)