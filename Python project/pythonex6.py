first_name = "Paavni"
last_name = "Rattan"

print "Name is: %s" %(first_name+ " " +last_name)
print "Her first name is %s and last name is %s" %(first_name,last_name)

x = "Today is Sunday:  %r"
y = False

print x % y 

print "Printing . 10 times"
print "." *10 

print "One line"
print "First line", 
print "Second line"

print "Two line"
print "First line"
print "Second line"

formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one", "two", "three", "four")
print formatter %("true", "false", "true", "true")
print formatter %(formatter,formatter, formatter, formatter)

print "Days of the week: \n Sunday, \n Monday, \n Tuesday"

print """Line after line. 
Line after line. 
Line after line. """

print "Printing single quotes \' \'" 
print "Printing double quotes \" \"" 