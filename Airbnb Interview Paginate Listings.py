# took 16 mins to come up with working O(n^2) solution
'''
You’re given an array of CSV strings representing search results.
Results are sorted by a score initially.
A given host may have several listings that show up in these results.
Suppose we want to show 12 results per page, but we don’t want the same host to
dominate the results. Write a function that will reorder the list so that a host shows up
at most once on a page if possible, but otherwise preserves the ordering. Your program
should return the new array and print out the results in blocks representing the pages.

    ["host_id,listing_id,score,city",
    "1,28,300.1,San Francisco",
    "4,5,209.1,San Francisco",
    "20,7,208.1,San Francisco",
    "23,8,207.1,San Francisco",
    "16,10,206.1,Oakland",
    "1,16,205.1,San Francisco",
    "1,31,204.6,San Francisco",
    "6,29,204.1,San Francisco",
    "7,20,203.1,San Francisco",
    "8,21,202.1,San Francisco",
    "2,18,201.1,San Francisco",
    "2,30,200.1,San Francisco",
    "15,27,109.1,Oakland",
    "10,13,108.1,Oakland",
    "11,26,107.1,Oakland",
    "12,9,106.1,Oakland",
    "13,1,105.1,Oakland",
    "22,17,104.1,Oakland",
    "1,2,103.1,Oakland",
    "28,24,102.1,Oakland",
    "18,14,11.1,San Jose",
    "6,25,10.1,Oakland",
    "19,15,9.1,San Jose",
    "3,19,8.1,San Jose",
    "3,11,7.1,Oakland",
    "27,12,6.1,Oakland",
    "1,3,5.1,Oakland",
    "25,4,4.1,San Jose",
    "5,6,3.1,San Jose",
    "29,22,2.1,San Jose",
    "30,23,1.1,San Jose"
]
'''
import random
# This class helps me to produce dummy data for my approches
class ProduceData(object):
    def oneHostDifferentListings(self):
        data = ["1,"+str(random.randint(1, 100))+","+str(score)+","+random.choice(["San Francisco","Oakland", "San Jose"]) for score in range(300, -1, -5)]
        return data

    def allDifferentHosts(self):
        data = [str(score/10)+","+str(random.randint(1, 100))+","+str(score)+","+random.choice(["San Francisco","Oakland", "San Jose"]) for score in range(500, -1, -10)]
        return data
    
class Page(object):
    def __init__(self):
        # hosts can be a hash table to ensure O(1) search time.
        self.hosts = []
        self.list = []

class Approch1(object):

    def findPage(self, pages, hostId):
        # if pages array empty, create new page and add it to array then return that page
        if not pages:
            p = Page()
            pages.append(p)
            return p
        # find first page where the current host is not present
        for page in pages:
            if (not(hostId in page.hosts) and len(page.list) < 12):
                return page
        # in case host is present in all pages, create new page
        p = Page()
        pages.append(p)
        return p

    def logic(self, data):
        # holds list of all pages
        pages = []
        for listing in data:
            hostId = listing.split(",")[0]
            page = self.findPage(pages, hostId)
            # Add host
            page.hosts.append(hostId)
            # Add listing
            page.list.append(listing)
        # print pages
        for page in pages:
            for listing in page.list:
                print listing
            print "\n"

class Page2(object):
    def __init__(self):
        self.listings = []
        self.pageNumber = None

class Approch2(object):
    def __init__(self):
        # key = host id, value => index of last page this host was present on.
        self.hashTable = {}
        # list of Pages
        self.pages = []
        self.fullPageIndex = 0

    def createPage(self):
        return Page2()

    def createPageUpdateHostIdInHashTable(self, hostId):
        page = self.createPage()
        page.pageNumber = len(self.pages)
        self.pages.append(page)
        # if its a new page the host won't be present on this page
        self.hashTable[hostId] = page.pageNumber
        return page

    def findPage(self, hostId):
        # first page or
        # if all pages are full create new page and return
        print "Current pages are", [page.listings for page in self.pages]
        if not self.pages or (len(self.pages) == self.fullPageIndex):
            return self.createPageUpdateHostIdInHashTable(hostId)           
        # find a page that does not have this host
        for i in range(self.fullPageIndex, len(self.pages)):
            if(hostId in self.hashTable):
                # either the previous pages are full or the host is present on these pages.
                if(self.hashTable[hostId] >= i):
                    continue
                else:                   
                    # if the last page the host was present on is less than the current page number,
                    # there is no way the host would be present on this page.
                    # also update the host id in hash
                    self.hashTable[hostId] = self.pages[i].pageNumber
                    return self.pages[i]
            else:            
                # if the host is not present in hash talbe it self then there is no way the host is present on this page.
                # also add the host to hash table
                self.hashTable[hostId] = self.pages[i].pageNumber
                return self.pages[i]
        # if our current host has been on all previous pages, or all our previous pages are full
        return self.createPageUpdateHostIdInHashTable(hostId)           
        
        

    def logic(self, data):
        for listing in data:
            hostId = listing.split(",")[0]
            print hostId
            page = self.findPage(hostId)
            print "hash table is", self.hashTable
            page.listings.append(listing)
            if(len(page.listings) == 12):
                self.fullPageIndex = self.fullPageIndex + 1
        for page in self.pages:
            for listing in page.listings:
                print listing
            print "\n"
    
# Main
data1 = ["host_id,listing_id,score,city",
    "1,28,300.1,San Francisco",
    "4,5,209.1,San Francisco",
    "20,7,208.1,San Francisco",
    "23,8,207.1,San Francisco",
    "16,10,206.1,Oakland",
    "1,16,205.1,San Francisco",
    "1,31,204.6,San Francisco",
    "6,29,204.1,San Francisco",
    "7,20,203.1,San Francisco",
    "8,21,202.1,San Francisco",
    "2,18,201.1,San Francisco",
    "2,30,200.1,San Francisco",
    "15,27,109.1,Oakland",
    "10,13,108.1,Oakland",
    "11,26,107.1,Oakland",
    "12,9,106.1,Oakland",
    "13,1,105.1,Oakland",
    "22,17,104.1,Oakland",
    "1,2,103.1,Oakland",
    "28,24,102.1,Oakland",
    "18,14,11.1,San Jose",
    "6,25,10.1,Oakland",
    "19,15,9.1,San Jose",
    "3,19,8.1,San Jose",
    "3,11,7.1,Oakland",
    "27,12,6.1,Oakland",
    "1,3,5.1,Oakland",
    "25,4,4.1,San Jose",
    "5,6,3.1,San Jose",
    "29,22,2.1,San Jose",
    "30,23,1.1,San Jose"
]
dataObj = ProduceData()
data2 = dataObj.allDifferentHosts()
data3 = dataObj.oneHostDifferentListings()

obj = Approch1()
obj.logic(data3)
print "****************************\n"
obj = Approch2()
obj.logic(data3)
