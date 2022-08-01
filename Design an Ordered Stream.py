# Design an Ordered Stream
# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream(object):

    def __init__(self, n):
        self.stream = [None for i in range(n+1)]
        self.ptr = 1
        """
        :type n: int
        """
        

    def insert(self, idKey, value):
        self.stream[idKey] = value
        # store old ptr
        oldPtr = self.ptr
        # increment the pointer
        while(self.ptr < len(self.stream) and self.stream[self.ptr] != None):
            self.ptr += 1
        # print from 0 to ptr
        answer = []
        for i in range(oldPtr, self.ptr):
            answer.append(self.stream[i])
        return answer
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
