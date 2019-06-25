#K Closest Points to Origin
#https://leetcode.com/problems/k-closest-points-to-origin/
import math
class Solution(object):
    def distanceFromOrigin(self, point):
        return math.sqrt((point[0]**2) + (point[1]**2))

    def putInHash(self, points):
        ht = {}
        for point in points:
            distance = self.distanceFromOrigin(point)
            if not(distance in ht):
                ht[distance] = [point]
            else:
                ht[distance].append(point)
        return ht

    def selectK(self, ht, K):
        output = []
        for key in sorted(ht):
            for point in ht[key]:
                if(K == 0):
                    return output
                output.append(point)
                K = K -1
        return output
                

    def kClosest(self, points, K):
        ht = self.putInHash(points)
        print self.selectK(ht, K)
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
#Main
obj = Solution()
obj.kClosest([[1,3],[-2,2]], 1)

obj = Solution()
obj.kClosest([[3,3],[5,-1],[-2,4]], 2)
