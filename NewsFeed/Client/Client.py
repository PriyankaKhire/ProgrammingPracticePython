import sys, time, socket, pickle
sys.path.append("../Class")
from User import User
sys.path.append("../Database")
from DatabaseHelper import DatabaseHelper
sys.path.append("../")
from Config import PortConfig

class Client(object):
    def __init__(self):
        self.userDbFile = '../Database/Users'
        self.serverName = 'MainServer'
        pc = PortConfig()
        port = pc.port[self.serverName]
        self.server = socket.socket()
        self.server.connect(('localhost', port))

    def createUser(self):
        # We create a dummy user for this client, in real world you'd either log in or sign up
        # but since we have already covered login and sign up in messaging app I won't do it here
        user = User()
        user.userName = 'Main User'
        user.userId = 100
        # We need to populate friends list, by default I am just gonna add all users from users database
        # to our main user's friend list so they can see the news feed.
        # in this the main user cannot create a post item to post it to their news feed
        user.friendList = DatabaseHelper().getAllKeys(self.userDbFile)
        while not user.friendList:
            print "Please start the create feed script, imma check on you again in 2 seconds"
            user.friendList = DatabaseHelper().getAllKeys(self.userDbFile)
            time.sleep(2)
        return user
        
    def run(self):
        print "#-"*14
        print "# Welcome to Chiddoo Social Media #"
        print "#-"*14
        user = self.createUser()
        self.server.send(pickle.dumps(user))

# Main
obj = Client()
obj.run()
