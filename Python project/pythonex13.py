from sys import argv

script, filename = argv

def printfile(f):
	print f.read()

def seekfile(f):
	print "Executing seek file ..."
	f.seek(0)

def readoneline(f):
	print f.readline()

fo = open(filename)

printfile(fo)
seekfile(fo)
readoneline(fo)

fo.close()