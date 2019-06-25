#Paste class
class Paste(object):
    def __init__(self, userId, text, fileName, folderName):
        self.userId = userId
        self.text = text
        self.fileName = fileName
        self.folderName = folderName
