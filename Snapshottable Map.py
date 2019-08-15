# https://leetcode.com/discuss/interview-question/358048/google-snapshottable-map
'''
Implement SnapshottableMap class.

class Snapshot {
	String get(String key);
}

class SnapshottableMap {
	void put(String key, String value);
	String get(String key);
	Snapshot createSnapshot();
	List<Snapshot> getSnapshots();
}
Example:

SnapshottableMap map = new SnapshottableMap();
Snapshot s0 = map.createSnapshot();

s0.get("name"); // null

map.put("name", "John");
map.put("country", "UK");
Snapshot s1 = map.createSnapshot();
 
s1.get("name"); // "John"
s1.get("country"); // "UK"
 
map.put("name", "Marta");
Snapshot s2 = map.createSnapshot();
 
s2.get("name"); // "Marta"
s2.get("country"; // "UK"
s1.get("name"); // "John"
'''
class Snapshot(object):
    def __init__(self):
        self.hashTable = None
        
    def get(self, key):
        if not key in self.hashTable:
            return None
        return self.hashTable[key]

class SnapshottableMap(object):
    def __init__(self):
        self.hashTable = {}
        self.snapshotList = []
        
    def put(self, key, value):
        self.hashTable[key] = value

    def get(self, key):
        if not key in self.hashTable:
            return None
        return self.hashTable[key]

    def createSnapshot(self):
        s = Snapshot()
        s.hashTable = self.hashTable.copy()
        self.snapshotList.append(s)
        return s

    def getSnapshots(self):
        return self.snapshotList

# Main
map1 = SnapshottableMap()
s0 = map1.createSnapshot()
print s0.get('name') #None

map1.put('name', 'John')
map1.put('country', 'UK')
s1 = map1.createSnapshot()

print s1.get('name') #John
print s1.get('country') #UK

map1.put('name', 'Marta')
s2 = map1.createSnapshot()

print s2.get('name') #Marta
print s2.get('country') #UK
print s1.get('name') #John


