import socket, threading, sys, pickle, os, time, datetime
sys.path.append("../Classes")
from Message import Message
from User import User
sys.path.append("../../")
from Config import PortConfig
sys.path.append("../Database")
from DatabaseHelper import DatabaseHelper

class Client(object):
    def __init__(self):
        self.userDatabase = '../Database/Users'
        self.currentUser = None
        self.welcomeMessage()
        self.reciever = self.selectFriendToChatWith()
        self.serverName = 'MessageStoreChatServer'
        pc = PortConfig()
        port = pc.port[self.serverName]
        self.server = socket.socket()
        self.server.connect(('localhost', port))
        #Send server your name so server can save it in a hash along with your conneciton id
        self.server.send(self.currentUser.userName)
        print self.server.recv(1024)
        #Send server reciever's name so server can pull previous chat history with that reciever
        self.server.send(self.reciever.userName)

    def selectFriendToChatWith(self):
        if not self.currentUser.friendList:
            self.getUsersToAddFriends()
        print "\nHere are your frinds"
        for i in range(len(self.currentUser.friendList)):
            friendObj = self.currentUser.friendList[i]
            print "="*50
            print friendObj.firstName, " ", friendObj.lastName
            print "Index Value: ", i
        print "="*50
        index = int(input('Please enter the index number of the friend you want to chat with '))
        while(index < 0 or index > len(self.currentUser.friendList)):
            index = int(input('Please enter a valid index number '))
        return self.currentUser.friendList[index]

    def getUsersToAddFriends(self):
        users = DatabaseHelper().getAllValues(self.userDatabase)
        print "Here are list of users "
        for i in range(len(users)):
            user = users[i]
            if(user.userName == self.currentUser.userName):
                continue
            print "-"*50
            print user.firstName, " ", user.lastName
            print "Index Value: ", i
        print "-"*50
        ch = 'y'
        while(ch.lower() == 'y'):
            #We want to add at least 1 friend
            friendIdexValue = int(input('Please type index value of the user you would like to add as a friend: '))
            while(friendIdexValue < 0 or friendIdexValue > len(users)):
                friendIdexValue = int(input('Invalid entry, please enter another index value: '))
            self.currentUser.friendList.append(users[friendIdexValue]) 
            ch = raw_input('Would you like to add another friend ? y/n ')
        #update current user in database
        DatabaseHelper().writeToHash(self.userDatabase, self.currentUser.userName, self.currentUser)

    def putMessage(self):
        sequenceNumber = 0
        while True:
            message = Message()
            message.message = raw_input()
            message.sender = self.currentUser.userName
            message.receiver = self.reciever.userName
            message.timeStamp = datetime.datetime.fromtimestamp(time.time())
            message.sequenceNumber = sequenceNumber
            message_string = pickle.dumps(message)
            self.server.send(message_string)
            sequenceNumber = sequenceNumber+1

    def processMessage(self, message):
        if(message == "ping"):
                self.server.send("ping")
        elif(message == "Ack"):
            return
        elif(message == "Delivered"):
            print "Delivered"
        else:
            message_obj = pickle.loads(message)
            print message_obj.sender, " at ",message_obj.timeStamp
            print message_obj.message, "\n"

    def getMessage(self):
        while True:
            message = self.server.recv(3072)
            self.processMessage(message)

    def ifUserExistsInDb(self, userName):
        #Ideally we would have a different database server do this but this is just easy on client side to code for now.
        #Realistically this should take place on server side.
        return DatabaseHelper().isKeyInHash(self.userDatabase, userName)

    def SignUP(self):
        print '-'*29
        print "|Welcome to Sign up page|"
        print '-'*29
        user = User()       
        user.firstName = raw_input("Enter your first name: ")
        user.lastName = raw_input("Enter your last name: ")
        user.email = raw_input("Enter email address: ")
        user.userName = raw_input("Enter desired user name: ")
        #find if the user name exist in database if so then prompt user to enter other user name
        while(self.ifUserExistsInDb(user.userName)):
            user.userName = raw_input("User name already taken, please enter another user name: ")
        # insert user in users database with key as user name and value as user object
        DatabaseHelper().writeToHash(self.userDatabase, user.userName, user)
        self.currentUser = user
        

    def LogIn(self):
        print '-'*26
        print "|Welcome to login page|"
        print '-'*26
        userName = raw_input("Enter your user name: ")
        #Search database to find the user with the user name, if not found then show error
        while not(self.ifUserExistsInDb(userName)):
            userName = raw_input("Invalid user name, please enter a valid user name: ")
        self.currentUser = DatabaseHelper().getValue(self.userDatabase, userName)

    def welcomeMessage(self):
        print "*"*47
        print "*           Welcome to Chiddoo Messenger            *"
        print "*    Please chose one of the following options     *"
        print "*                     1 -> Sign up                                   *"
        print "*                    2 -> Log in                                      *"
        print "*"*47
        option = int(raw_input("Enter option 1 or 2 "))
        if(option == 1):
            self.SignUP()
        else:
            self.LogIn()

    def run(self):
        print "User ", self.currentUser.userName, " now ready to send messages to receiver ", self.reciever.userName
        background_thread = threading.Thread(target=self.putMessage)
        background_thread.daemon = True
        background_thread.start()
        self.getMessage()
    
#Main
obj = Client()
obj.run()
