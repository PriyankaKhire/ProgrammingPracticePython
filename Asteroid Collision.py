#Asteroid Collision
#https://leetcode.com/problems/asteroid-collision/
class Solution(object):
    def __init__(self):
        self.stack = []

    def logic(self, asteroids):
        for asteroid in asteroids:
            #if our current asteroid is positive then put it in stack.
            if(asteroid >= 0):
                self.stack.append(asteroid)
            else:
                #if our current asteroid is negative then
                #if our current asteroid is bigger than the top asteroid of stack the pop it from stack
                while(self.stack and abs(self.stack[-1]) < abs(asteroid) and self.stack[-1] >=0):
                    self.stack.pop()
                #if top of stack is bigger than current asteroid than skip rest of the steps
                if(self.stack and abs(self.stack[-1]) > abs(asteroid) and self.stack[-1] >=0):
                    continue
                #if current asteroid is equal to stack top asteroid
                if(self.stack and abs(self.stack[-1]) == abs(asteroid) and self.stack[-1] >=0):
                    self.stack.pop()
                    continue
                #if stack is empty or is carrying negative asteroids.
                if(not self.stack or self.stack[-1] < 0):
                    self.stack.append(asteroid)
        print self.stack
        
    def asteroidCollision(self, asteroids):
        self.logic(asteroids)
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

#Main
obj1 = Solution()
obj1.asteroidCollision([10, 2, -5])

obj2 = Solution()
obj2.asteroidCollision([5, 10, -5])

obj3 = Solution()
obj3.asteroidCollision( [8, -8])

obj3 = Solution()
obj3.asteroidCollision( [-2, -1, 1, 2])

obj4 = Solution()
obj4.asteroidCollision( [-2,-2,-1,-2])
