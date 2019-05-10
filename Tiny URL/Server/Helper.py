#Helper functions for server
class Helper(object):
    
    def removePrefix(self, prefix, string):
        if(string.startswith(prefix)):
            return string[len(prefix):]
        return string

    def removeCommonPrefixes(self, url):
        prefixes = ["https://","http://","www."]
        for prefix in prefixes:
            url = self.removePrefix(prefix, url)
        return url
