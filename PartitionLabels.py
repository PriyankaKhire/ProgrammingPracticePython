#Partition Labels
#https://leetcode.com/problems/partition-labels/description/

class partitionLables(object):
    def __init__(self, s):
        self.s = s
        #This hash map will have key as letter and value as start and end position of that letter
        self.hash_map = {}

    #Scans string s and puts it in hash table
    def scan_s(self):
        for i in range(len(self.s)):
            if(self.s[i] not in self.hash_map):
                self.hash_map[self.s[i]] = [i, i]
            else:
                self.hash_map[self.s[i]][1] = i
        print self.hash_map

    def compare_with_output(self, output, range_i, i):
        add_new_flag = False
        extend_flag = False
        extend_range = []
        print output
        for output_range in output:
            print output_range
            if(output_range[0] <= range_i[0] and range_i[1] <= output_range[1]):
                print "for output range "+str(output_range)
                print "its within"
                return output
            elif(output_range[1] < range_i[0] ):
                #output.append(self.hash_map[self.s[i]])
                print "for output range "+str(output_range)
                print "we add new range"
                add_new_flag = True
            elif(output_range[0] < range_i[0] and output_range[1] > range_i[0] and output_range[1] < range_i[1]):
                #output_range[1] = range_i[1]
                print "for output range "+str(output_range)
                print "we extend range"
                extend_flag = True
                extend_range = output_range
'''
            if(extend_flag == True):
                print "extending"
                output.remove(extend_range)
                extend_range[1] = range_i[1]
                output.append(extend_range)
                return output
            if(add_new_flag == True):
                print "adding"
                output.append(self.hash_map[self.s[i]])
                return output
'''                

    def partition_string(self):
        self.scan_s()
        output = []
        #Put first range in output
        output.append(self.hash_map[self.s[0]])
        for i in range(len(self.s)):
            range_i = self.hash_map[self.s[i]]
            print range_i
            print self.s[i]
            output = self.compare_with_output(output, range_i, i)
            print output
            print "---"
        print output
            

#Main Program
obj = partitionLables("ababcbacadefegdehijhklij")
obj.partition_string()
