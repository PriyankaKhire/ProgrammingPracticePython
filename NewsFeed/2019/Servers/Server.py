#Server
import sys, socket, pickle, random, time
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
        self.seenPostsFile = '../Database/SeenPosts'
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
        # return the 10 most recent posts, please check the news feed ranking image for more info on this.
        return userObj.posts[-10:]

    def storeInSeenPostsFile(self, user, friendUserName, posts):
        # here is the structure of the seen posts file:
        # Key -> userName Value -> {friendUserName: [postId1... postIdN]}
        friendHashTable = DatabaseHelper().getValue(self.seenPostsFile, user.userName)
        if not friendHashTable:
            DatabaseHelper().writeToHash(self.seenPostsFile, user.userName, {friendUserName: posts})
            return
        if not (friendUserName in friendHashTable):
            friendHashTable[friendUserName] = posts
        else:
            friendHashTable[friendUserName] = friendHashTable[friendUserName] + posts
        DatabaseHelper().writeToHash(self.seenPostsFile, user.userName, friendHashTable)

    def checkForPostDuplicacy(self, user, friendUserName, posts):
        # after getting these posts, we'd wanna not get these same posts again coz the user's already
        # seen them, so it's better to store these posts in a database and compare these posts to that
        # to make sure we are not serving duplicate posts.
        friendHashTable = DatabaseHelper().getValue(self.seenPostsFile, user.userName)
        # if friend hash table empty
        if not friendHashTable:
            return posts
        # if friend not present in hash table
        if not(friendUserName in friendHashTable):
            return posts
        # if friend present in hash table, compare posts with seen posts and remove seen posts
        seenFriendPosts = friendHashTable[friendUserName]
        return list(set(posts) - set(seenFriendPosts))

    def getPostIds(self, posts):
        return [post.id for post in posts]

    def getPostsFromPostIds(self, postIds, posts):
        return [post for post in posts if post.id in postIds]

    def getFriendsFeed(self, user):
        feed = []
        for friendName in user.friendList:
            friendPosts = self.getPost(friendName)
            postIds = self.getPostIds(friendPosts)
            unSeenPostIds = self.checkForPostDuplicacy(user, friendName, postIds)
            unSeenFriendPosts = self.getPostsFromPostIds(unSeenPostIds, friendPosts)
            feed = feed + unSeenFriendPosts
            self.storeInSeenPostsFile(user, friendName, unSeenPostIds)
        # Randomize the array, coz that's how I wanna rank the feed
        random.shuffle(feed)
        return feed

    def sendFeed(self, feed, connection):
        # Since I cannot send the entire feed at once I have this alternative
        for post in feed:
            connection.send(pickle.dumps(post))
            time.sleep(2)
        connection.send("EndOfFeed")

    def AcceptConnections(self):
        print "Server Started..."
        try:
            connection, address = self.server.accept()
            user = connection.recv(10000)
            feed = self.getFriendsFeed(pickle.loads(user))
            self.sendFeed(feed, connection)
            connection.close()            
        except Exception as e:
            print "Exception:", e
        
        
# Main
obj = Server()
obj.AcceptConnections()
