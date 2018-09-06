#Task Scheduler
#https://leetcode.com/problems/task-scheduler/description/
class Solution(object):
    def __init__(self):
        self.hash = {}
        self.taskNames = []
        
    def insertTasksInHash(self, tasks):
        for task in tasks:
            if not(task in self.hash):
                self.hash[task] = 1
                self.taskNames.append(task)
            else:
                self.hash[task] = self.hash[task]+1

    def formulateOutput(self, n):
        field = []
        taskFieldCount = 0
        output = []
        #take n+1 tasks out on field
        for i in range(n+1):
            if(self.taskNames):
                field.append(self.taskNames.pop(0))
                taskFieldCount = taskFieldCount+1
            else:
                field.append('idle')
        #begin formulating output
        while (taskFieldCount > 0):
            for i in range(len(field)):
                task = field[i]
                output.append(task)
                if(task != 'idle'):
                    self.hash[task] = self.hash[task]-1
                    if(self.hash[task] == 0):
                        #replace with existing tasks or if no other existing tasks then replace with idle
                        if(self.taskNames):
                            field[i] = self.taskNames.pop(0)
                        else:
                            field[i] = 'idle'
                            taskFieldCount = taskFieldCount-1
        while(output[-1] == "idle"):
            output.pop()
        return len(output)
           
    
    def leastInterval(self, tasks, n):
        self.insertTasksInHash(tasks)
        return self.formulateOutput(n)
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

#Main
o = Solution()
print o.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)
