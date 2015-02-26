print "*****CALCULATOR*****"

def addfunc(a, b):
	print "adding"
	return a+b

def multiplyfunc(a, b):
	print "multiplying"
	return a*b

no1 = raw_input("Enter first no: ")
no2 = raw_input("Enter second no: ")

no1 = int(no1)
no2 = int(no2)
print "Sum %r" % (addfunc(no1, no2))
print "Product %r" % (multiplyfunc(no1, no2))
