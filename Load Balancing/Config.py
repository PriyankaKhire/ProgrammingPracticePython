#Config file specifing which server has what port number
class ServerConfig(object):
    def __init__(self):
        #key is server name and value is port number
        self.port = {
            'Server1':1041,
            'Server2':2002,
            'Server3':3003,
            'Server4':4004,
            'Server5':5005,
            'Server6':6006,
            'Server7':7007,
            'Server8':8008,
            'Server9':9009,
            'Server10':1010
            }

#Config file specifing which approch server has what port number
class ApprochConfig(object):
    def __init__(self):
        #key is Approch Server name and value is port number
        self.port = {
            'Approch1':94,
            'Approch2':200
            }
        
#Config file specifying the data for client file
class ClientData(object):
    def __init__(self):
        self.data = {
            0:'aaa',
            1:'bbb',
            2:'ccc',
            3:'ddd',
            4:'eee',
            5:'fff',
            6:'ggg',
            7:'hhh',
            8:'iii',
            9:'jjj',
            10:'kkk'
            }
