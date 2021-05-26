import sys, random, datetime, time, threading
from os import path
from thread import *
sys.path.append("Class")
from User import User
from Post import Post
sys.path.append("Database")
from DatabaseHelper import DatabaseHelper
sys.path.append("../ASCII Images")
from AsciiImages import AsciiImages
sys.path.append("..")
from RandomSentenceGenerator import RandomSentenceGenerator
from Names import Names
    
class CreateUsers(object):
    def __init__(self):
        self.userDbFile = 'Database/Users'

    def createUser(self, userGender, userId):
        user = User()
        user.firstName = Names().get_first_name(userGender)
        user.lastName = Names().get_last_name()
        user.email = user.firstName+'.'+user.lastName+'@SnailMail.com'
        user.userName = user.firstName[:3].lower()+user.lastName[:3].lower()
        user.userId = userId
        return user

    def insertUserInDB(self, user):
        # Note: if there are duplicate users, we dont insert them in database
        db = DatabaseHelper()
        if not(db.isKeyInHash(self.userDbFile, user.userName)):
            db.writeToHash(self.userDbFile, user.userName, user)


    def populateDB(self):
        # create 5 female users and 5 male users
        users = [self.createUser('female',i) for i in range(5)] + [self.createUser('male',i+5) for i in range(5)]
        # insert user into database
        for user in users:
            self.insertUserInDB(user)
        return users

class GenerateFeed(object):
    def __init__(self):
        self.users = None
        createUsers = CreateUsers()
        # if user's file exist then get users from there
        if not (path.exists(createUsers.userDbFile)):
            self.users = createUsers.populateDB()
        else:
            self.users = DatabaseHelper().getAllValues(createUsers.userDbFile)
        

    def getPostContent(self):
        ai = AsciiImages()
        rsg = RandomSentenceGenerator()
        return random.choice([['image', ai.RandomImage()], ['text', rsg.RandomSentence()]])

    def createPostObject(self, userName, postId, name):
        post = Post()
        post.userName = userName
        post.name = name
        content = self.getPostContent()
        post.contentType = content[0]
        if(content[0] == 'image'):
            post.picture = content[1]
        else:
            post.text = content[1]
        post.timeStamp = str(datetime.datetime.now())
        post.id = postId
        return post

    def userPost(self, user):
        post = self.createPostObject(user.userName, len(user.posts), str(user.firstName+" "+user.lastName))
        print user.firstName,user.lastName," "*5,'at',post.timeStamp
        if(post.contentType == 'image'):
            print post.picture
        else:
            print post.text
        # append post object to user object's posts list
        user.posts.append(post)
        # store it in database
        DatabaseHelper().writeToHash(CreateUsers().userDbFile, user.userName, user)

    def userThread(self, user):
        while True:
            self.userPost(user)
            time.sleep(random.randint(10, 30))

    def feed(self):
        for user in self.users:
            start_new_thread(self.userThread, (user,))
            time.sleep(2)
        # this little hack to keep it running in cmd
        while True:
            time.sleep(5)


# Main
obj = GenerateFeed()
obj.feed()
