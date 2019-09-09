#Simulate Diplomacy
'''
Input(army_name, location, action)

action:
    Move(new_location):- Move the current army to new location.
    if there is already another army at this location then:
        army with higher strength wins and stays at that location
        if both armies have same strength, then both disappear
    Hold(): - Stay at the same location
    Support(army_name):- Support another army, the supported army has +1 strength

Initially all armies have same strength.
'''
class Army(object):
    def __init__(self, name, location, strength):
        self.name = name
        self.location = location
        self.strength = strength
        # list of armies that support our current army.
        self.support = []

class Diplomacy(object):
    def __init__(self):
        # key -> army name, value -> army object
        self.armies = {}
        #key -> location name, value -> army guarding this location.
        self.location ={}

    def Hold(self, army_name):
        print "current army",army_name,"Stays at same locaiton"
        return

    def Support(self, supportingArmy, supportedArmy):
        self.armies[supportedArmy].support.append(supportingArmy)
        self.armies[supportedArmy].strength = self.armies[supportedArmy].strength + 1

    def Move(self, army_name, location):
        # if no such army present
        if not(army_name in self.armies):
            print "No such army present"
            return
        if(self.armies[army_name].location == location):
            return
        # if there is no army present at this location
        if(self.location[location] == False):
            self.location[location] = self.armies[army_name]
            return
        # if there is an army present at this location, then compare their strength
        if(self.location[location].strength == self.armies[army_name].strength):
            # if both have same strength, then both disappear
            del self.armies[army_name]
            del self.armies[self.location[location].name]
            return
        # else the army with lower strength disapears
        if(self.location[location].strength < self.armies[army_name].strength):
            del self.armies[self.location[location].name]
            self.location[location] = self.armies[army_name]
        else:
            del self.armies[army_name]

# Main
obj = Diplomacy()
obj.location = {
    'San Fransisco': False,
    'Seattle': False,
    'Chandler':False,
    'DuPont':False,
    'Riverside':False
                }
obj.armies = {
    'Future':Army('Future', 'San Fransisco', 1),
    'Present':Army('Present', 'Seattle', 1),
    'NewGrad':Army('NewGrad', 'Chandler', 1),
    'Intern':Army('Intern', 'DuPont', 1),
    'Student':Army('Student', 'Riverside', 1)
    }
obj.location['San Fransisco'] = obj.armies['Future']
obj.location['Seattle'] = obj.armies['Present']
obj.location['Chandler'] = obj.armies['NewGrad']
obj.location['DuPont'] = obj.armies['Intern']
obj.location['Riverside'] = obj.armies['Student']
print obj.location
obj.Support('NewGrad', 'Present')
print obj.armies['Present'].strength
obj.Move('Present', 'San Fransisco')
print obj.location['San Fransisco'].name
