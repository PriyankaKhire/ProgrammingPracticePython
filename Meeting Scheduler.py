# Meeting Scheduler
# https://leetcode.com/problems/meeting-scheduler/
class Solution(object):
    def sortSlots(self, slot1, slot2):
        # organise them by lowest start time
        slotList = sorted([slot1, slot2], key=lambda x:x[0])
        return slotList[0], slotList[1]
        
    def isMergable(self, slot1, slot2):
        s1, s2 = self.sortSlots(slot1, slot2)
        if(s1[1] > s2[0]):
            return True
        return False
    
    def findCommonFreeSlot(self, s1, s2):
        # common slot is time that starts later and time that ends earlier
        return [max(s1[0], s2[0]), min(s1[1], s2[1])]
    
    def getAllFreeSlots(self, slots1, slots2):
        i = 0
        j = 0
        freeSlots = []
        while(i<len(slots1) and j<len(slots2)):
            if(self.isMergable(slots1[i], slots2[j])):
                freeSlot = self.findCommonFreeSlot(slots1[i], slots2[j])
                freeSlots.append(freeSlot)
            # Increment only that index that ends first
            if(slots1[i][1] < slots2[j][1]):
                i = i+1
            else:
                j = j+1
        return freeSlots
            
        
    def minAvailableDuration(self, slots1, slots2, duration):
        # edge case
        if not (slots1 or slots2):
            return []
        # Sort the slots according to start time
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        # get all the free slots
        freeSlots = self.getAllFreeSlots(slots1, slots2)
        # find first free slot that encompasses the duration
        for slot in freeSlots:
            if(slot[1] - slot[0] >= duration):
                return [slot[0], slot[0]+duration]
        return []
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        
