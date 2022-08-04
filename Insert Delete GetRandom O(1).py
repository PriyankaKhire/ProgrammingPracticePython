# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
class RandomizedSet(object):

    def __init__(self):
        # key = val value = index of val in array List.
        self.hashMap = {}
        self.arrayList = []

    def insert(self, val):
        if (val not in self.hashMap):
            self.arrayList.append(val)
            self.hashMap[val] = len(self.arrayList)-1
            return True
        return False
        """
        :type val: int
        :rtype: bool
        """

    def remove(self, val):
        if (val in self.hashMap):
            # get index of value
            index = self.hashMap[val]
            # copy the last value of array list to this index
            self.arrayList[index] = self.arrayList[-1]
            # update index of last val in hash map
            self.hashMap[self.arrayList[-1]] = index
            # delete last item from array list
            self.arrayList.pop()
            # delete val from hash map
            del self.hashMap[val]
            # return true
            return True
        return False
        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return random.choice(self.arrayList)
        """
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
