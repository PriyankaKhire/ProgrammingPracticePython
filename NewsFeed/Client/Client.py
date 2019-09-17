import sys, time, socket, pickle
sys.path.append("../Class")
from User import User
from Post import Post
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

    def displayPost(self, post):
        postObj = pickle.loads(post)
        print "*"*80
        print '{:^80}'.format(postObj.name+" "*5+"at"+str(postObj.timeStamp))
        if(postObj.text):
            print '{:^80}'.format(postObj.text)
        else:
            print postObj.picture
        print "*"*80
        print "\n"

    def getFeed(self):
        post = self.server.recv(1024)
        while(post != "EndOfFeed"):
            self.displayPost(post)
            post = self.server.recv(1024)
        
    def run(self):
        print '{:^78}'.format("#-"*14)
        print '{:^85}'.format("# Welcome to Chiddoo Social Media #")
        print '{:^78}'.format("#-"*14)
        user = self.createUser()
        self.server.send(pickle.dumps(user))
        try:
            self.getFeed()
        except Exception as e:
            print e

# Main
obj = Client()
obj.run()
