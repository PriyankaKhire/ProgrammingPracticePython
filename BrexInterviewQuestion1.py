# -*- coding: utf-8 -*-
# Brex interview CSV parser
'''
Given the following log, output it into CSV format
Input:
timestamp="Wed Jun 06 2019 22:00:21" message="test message" id ="1" field_1="test 1"
timestamp="Wed Jun 06 2019 22:00:22" message="test" id="2" field_2="test 2" filed_3="test 2"
timestamp="Wed Jun 06 2019 22:00:23" message="test message" id="3" field_4="test 3"
timestamp="Wed Jun 06 2019 22:00:24" message="test" id="4" field_5= "test 4" filed_6="test 4"
Output:
id,timestamp,message,field_1,field_2,field_3,field_4,field_5,field_6
1, Wed Jun 06 2019 22:00:21,test,test 1,,,,,
‍‌‌‌‌‌‌‍‌‌‍‍‌‌‌‌‍‌2, Wed Jun 06 2019 22:00:22,test,,test 2,test 2,,,,
3, Wed Jun 06 2019 22:00:23,test,,,,test 3 ,,
4, Wed Jun 06 2019 22:00:24,test,,,,,test 4,test 4
'''
class TimeStamp(object):
    def __init__(self):
        self.day = None
        self.month = None
        self.date = None
        self.year = None
        self.hour = None
        self.minute = None
        self.second = None
        
class CSVObject(object):
    def __init__(self):
        self.timeStamp = None
        self.message = None
        self.id = None
        self.fields = {}

    def getTimeStamp(self):
        tsObj = TimeStamp()
        tsSplit = self.timeStamp.split(" ")
        tsObj.day = tsSplit[0]
        tsObj.month = tsSplit[1]
        tsObj.date = int(tsSplit[2])
        tsObj.year = int(tsSplit[3])
        time = tsSplit[4].split(":")
        tsObj.hour = int(time[0])
        tsObj.minute = int(time[1])
        tsObj.second = int(time[2])
        self.timeStamp = tsObj
            
        
class CSVParser(object):
    def __init__(self):
        self.CSVObjects = []
        
    def splitFields(self, line):
        csvObj = CSVObject()
        lineFields = line.split('"')
        index = 0
        while(index < len(lineFields)):
            if (lineFields[index].strip().startswith("timestamp")):
                csvObj.timeStamp = lineFields[index+1]
            if (lineFields[index].strip().startswith("message")):
                csvObj.message = lineFields[index+1]
            if (lineFields[index].strip().startswith("id")):
                csvObj.id = int(lineFields[index+1])
            if (lineFields[index].strip().startswith("field")):
                csvObj.fields[int(lineFields[index].strip()[:-1][-1])] = lineFields[index+1]
            index = index+1
        self.CSVObjects.append(csvObj)
        # Create time stamp object
        csvObj.getTimeStamp()

    def parse(self, input_log):
        for line in input_log:
            self.splitFields(line)
        # you can write code to sort by id, time stamp and print etc.

# Main
obj = CSVParser()
obj.parse([
    'timestamp="Wed Jun 06 2019 22:00:21" message="test message" id ="1" field_1="test 1"',
    'timestamp="Wed Jun 06 2019 22:00:22" message="test" id="2" field_2="test 2" field_3="test 2"',
    'timestamp="Wed Jun 06 2019 22:00:23" message="test message" id="3" field_4="test 3"',
    'timestamp="Wed Jun 06 2019 22:00:24" message="test" id="4" field_5= "test 4" field_6="test 4"'
    ])
