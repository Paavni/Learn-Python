from sys import argv 

#name, first_var, second_var = argv

#print "Name of script" , name 

#print "1. " , first_var 
#print "2." , second_var 

###

name_script, name = argv

print "Hi %s" % name
print "I am the %s script" % name_script
print "What is your age %s" % name
age = raw_input()
print "What is your location:"
location = raw_input('>') 

print "%s stays in %r and is %r years old" %(name, location, age)

