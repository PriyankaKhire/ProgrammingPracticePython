#Server
from Helper import Helper
class Server(object):
    def __init__(self):
        self.id = 1
        self.helper = Helper()

    def shortenURL(self, url):
        url = self.helper.removeCommonPrefixes(url)
        print url    

#Main
obj = Server()
obj.shortenURL("www.google.com")
