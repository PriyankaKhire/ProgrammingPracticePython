#Timer
#https://leetcode.com/discuss/interview-question/350166/google-onsite-timer/319457
'''
Given the following class with 2 methods

class MySystem {
    
    /**
     * Waits durationMillis milliseconds then runs the callback.
     *
     * Only one timer can be pending at one time. If called again before the
     * duration expires, the original timer is overwritten without running
     * callback.
    */
    static void setTimer(long durationMillis, Runnable callback);

    /** Returns the current time in milliseconds since system boot. */
    static long getCurrentTimeMillis();
    
}
Use these methods to implement the 3rd method to support multiple timers:

/**
 * Waits durationMillis milliseconds then runs the callback.
 *
 * Supports multiple concurrent timers. Calling addTimer will not break
 * any previously started timers.
 */
void addTimer(long durationMillis, Runnable callback);
Usage is as follows:

MySystem sys = new MySystem(); 
sys.addTimer(100, runnable1); 
Thread.sleep(50);
sys.addTimer(100, runnable2);
'''
import time
import threading

class RunJob(object):
    def __init__(self, durationMillis, callback):
        self.durationMillis = durationMillis
        self.callback = callback
        self.timeJobStarted = None
        
# Note: this is just a sample implimentation to help me run the code.
class Runnable(object):
    def __init__(self, callback):
        self.callback = callback

    def run(self):
        print "\nRunning the job", self.callback
        
class MySystem(object):
    def __init__(self):
        self.q = []
        self.hasProcessingStarted = False
        self.thread = threading.Thread(target=self.processJob)
        self.thread.daemon = True           
    
    # Note: this is just a sample implimentation to help me run the code.
    def setTimer(self, durationMillis, callback):
        # Waits durationMillis milliseconds then runs the callback.
        print "Set timer is sleeping for",durationMillis,"milliseconds"
        time.sleep(durationMillis/1000)
        callback.run()

    # Note: this is just a sample implimentation to help me run the code.
    def getCurrentTimeMillis(self):
        # Returns the current time in milliseconds
        return int(round(time.time() * 1000))

    def processJob(self):
        print "\nTrying to process job in background while you add stuff to the queue"
        self.hasProcessingStarted = True
        while(self.q):
            # If no jobs have been scheduled, then schedule it
            if(self.q[0].timeJobStarted == None):
                self.setTimer(self.q[0].durationMillis, self.q[0].callback)
                # There might be some delay of few milliseconds when I update timeJobStarted
                self.q[0].timeJobStarted = self.getCurrentTimeMillis()
            else:
                # get the current time and check has the specified milliseconds in the job passed ?
                if(self.q[0].durationMillis <= (self.getCurrentTimeMillis() - self.q[0].timeJobStarted)):
                    self.q.pop(0)
        self.hasProcessingStarted = False

    def addTimer(self, durationMillis, callback):
        print "\nAdded job to the queue"
        job = RunJob(durationMillis, callback)
        self.q.append(job)
        # If the queue is already not being processed then start processing it
        # else you have already added a task to the queue so let processJob take care of it, no need to start new thread for it.
        if not(self.hasProcessingStarted):
            self.thread.start()    
        

# Main
obj = MySystem()
obj.addTimer(5000, Runnable('callback1'))
obj.addTimer(5000, Runnable('callback2'))
    
