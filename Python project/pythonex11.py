'''
from sys import argv

script, filename = argv

text = open(filename, 'w')

text.truncate()

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")

print("writing now..........")
text.write(line1)
text.write("\n")
text.write(line2)

text.close()

text = open(filename)
print text.read()
print text.readline()
'''

from sys import argv
from os.path import exists 

script, file1, file2 = argv

print "Source file %s || Target file %s " %(file1, file2)
text = open(file1)
txt = text.read() 
print txt
print len(txt)

print "Does the target file exist %r" % exists(file2)
print "If exists press enter else press Ctrl-C/C^"
raw_input()

textwrite = open(file2, 'w')
textwrite.write(txt)
textwrite.close()
text.close()


