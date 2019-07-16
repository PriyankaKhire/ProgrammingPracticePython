#Embedding NP-Complete problems in restaurent orders
#https://xkcd.com/287/
class Solution(object):
    def logic(self, appetizers, remainingMoney, selectedAppetizers):
        if(remainingMoney == 0):
            print selectedAppetizers
            return 
        for appetizer in appetizers:
            if(remainingMoney-appetizers[appetizer] >= 0):
                self.logic(appetizers, remainingMoney-appetizers[appetizer], selectedAppetizers+[appetizer])
        
    def appetizerList(self, appetizers, money):
        self.logic(appetizers, money, [])
        '''
        :type appetizers: HashTable{string : float}
        :type money: float
        :rtype: List[string]
        '''
#Main
appetizers = {
    'Mixed Fruit' : 2.15,
    'French Fries' : 2.75,
    'Side Salad' : 3.35,
    'Hot Wings' : 3.55,
    'Mozzarella Sticks' : 4.20,
    'Sampler Plate' : 5.80
    }
obj = Solution()
obj.appetizerList(appetizers, 15.05)
