# Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/description/

class Logger(object):

    def __init__(self):
        self.messages = {}
    
    # returns true if we have seen this message and that timestamp >= message time
    # returns true if we haven't seen the message as we are allowed to print it.
    def seenMessageAllowedToPrint(self, message, ts):
        if (message not in self.messages):
            self.messages[message] = ts+10
            return True
        originalTS = self.messages[message]
        if (ts >= originalTS):
            # update the time stamp
            self.messages[message] = ts+10
            return True
        return False

    def shouldPrintMessage(self, timestamp, message):
        return self.seenMessageAllowedToPrint(message, timestamp)
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
