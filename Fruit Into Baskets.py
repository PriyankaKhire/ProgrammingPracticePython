#Fruit Into Baskets
#https://leetcode.com/problems/fruit-into-baskets/
#https://www.youtube.com/watch?time_continue=4&v=kHQXRHpxI10
#Problem explanation:
# you are given 2 baskets, each basket can carry only 1 type of fruit but it can have any quantity of
# that type of fruit.
#if your first basket is carrying fruit of type mango then it can only carry mangoes and it can carry
#infinite mangoes. you cannot add apples in to this fruit basket.
# so now you are given an array where types of fruit is represented by numbers
# example [1,2,1] so 1 is a type of fruit 2 is a type of fruit, it doesnt mean that tree at index 0 has
# only 1 fruit. it means tree at index 0 has fruit type 1.
#now when you start from an index,  you can perform 2 things
#1) look at the type of fruit, if one of your baskets doesnt have any fruit in it you can add that type of
#fruit to that basket and move to next index.
#2)if the current index has fruit type that is not present in any of your given baskets (both your baskets are
#filled with differtent type of fruites) then you need to stop.
#given an arrya like that and 2 baskets, specify how many total fruits can you collect.
#Example: [3,3,3,1,2,1,1,2,3,3,4]
#let fruit type 1 => apple , 2 =>  mango, 3 => orange, 4 => banana
# so now our array becomes [orange,orange,orange,apple,mango,apple,apple,mango,orange,orange,banana]
#if I start at index 0 to collect fruits I can first collect 1 orange and I move to index 1
#here i also see orange so i collect it in my first basket that already has orange.
#at index 2 there is orange so I collect it
#at index 3 there is apple and I dont have anything in my second basket, so I collect it.
#at index 4 i see there is a mango tree and my first basket has 3 oranges and second basket has 1 apple
# I cannot add any new fruit so I stop and my end result is total 4 fruits
#but if I start collecting fruits from index 3 then I can collect 3 apples and 2 mangoes so total 5 fruits
# thus the problem boils down to finding a sub array that has most number of any 2 types of fruits.
class Backtracking(object):
    def __init__(self, fruitArray):
        self.fruitArray = fruitArray
        self.output = 0
        self.outputIndex = None

    def recurrse(self, index, basket1, basket2, basket1FruitType, basket2FruitType):
        #print "Index = ", index, "Basket1 Count = ", basket1, "Basket2 Count = ",basket2, "Basket 1 type ", basket1FruitType, "Basket 2 type", basket2FruitType
        if((index >= len(self.fruitArray)) or (basket1FruitType != None and basket2FruitType != None) and (basket1FruitType != self.fruitArray[index] and basket2FruitType != self.fruitArray[index] )):
                #print "Total fruits collected is ", (basket1+basket2)
                if(self.output < (basket1+basket2)):
                    self.output = (basket1+basket2)
                    self.outputIndex = index
                return 
        if(basket1FruitType == None or basket1FruitType == self.fruitArray[index]):
            basket1FruitType == self.fruitArray[index]
            self.recurrse(index+1, basket1+1, basket2, self.fruitArray[index], basket2FruitType)
        if(basket1FruitType != None and (basket2FruitType == None or basket2FruitType == self.fruitArray[index])):
            basket2FruitType == self.fruitArray[index]
            self.recurrse(index+1, basket1, basket2+1, basket1FruitType, self.fruitArray[index])

    def logic(self):
        print "For array ", self.fruitArray
        for index in range(len(self.fruitArray)):
            #print "When starting from index ", index
            self.recurrse(index, 0, 0, None, None)
        print "Max fruits collected is ", self.output, "at index ", self.outputIndex-self.output
            

#Main
obj1 = Backtracking([3,3,3,1,2,1,1,2,3,3,4])
obj1.logic()

obj2 = Backtracking([1,2,3,2,2])
obj2.logic()

obj3 = Backtracking([0,1,2,2])
obj3.logic()

obj4 = Backtracking([1,2,1])
obj4.logic()
