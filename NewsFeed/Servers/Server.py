#Server
import sys, socket, pickle
sys.path.append("../")
from Config import PortConfig
sys.path.append("../Class")
from User import User
sys.path.append("../Database")
from DatabaseHelper import DatabaseHelper

class Server(object):
    def __init__(self):
        self.name = 'MainServer'
        self.userDbFile = '../Database/Users'
        self.pc = PortConfig()
        port = self.pc.port[self.name]
        self.server = socket.socket()
        self.server.bind(('localhost', port))
        self.server.listen(5)

    def getPost(self, userName):
        # if this was a real system, I wouln't be storing the post objects inside user object
        # realistically I'd be storing the posts in a saparate database table where the primary key is userId
        # and the value is the list of posts, since I am lazy I have just stored everything in one database.
        userObj = DatabaseHelper().getValue(self.userDbFile, userName)
        print userObj.firstName, userObj.lastName
        

    def getFriendsFeed(self, user):
        for friendName in user.friendList:
            self.getPost(friendName)

    def AcceptConnections(self):
        print "Server Started..."
        connection, address = self.server.accept()
        user = connection.recv(2048)
        connection.close()
        self.getFriendsFeed(pickle.loads(user))
        
        
# Main
obj = Server()
obj.AcceptConnections()
