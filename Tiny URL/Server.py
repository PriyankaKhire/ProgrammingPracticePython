#Server
class Server(object):
    def __init__(self):
        self.id = 1

    def removePrefix(self, prefix, string):
        if(string.startswith(prefix)):
            return string[len(prefix):]
        return string

    def removeCommonPrefixes(self, url):
        prefixes = ["https://","http://","www."]
        for prefix in prefixes:
            url = self.removePrefix(prefix, url)
        return url

    def shortenURL(self, url):
        url = self.removeCommonPrefixes(url)
        
        

#Main
obj = Server()
obj.shortenURL("www.google.com")
