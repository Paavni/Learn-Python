"""
people = 20 
animals = 15 
birds = 30 

if people > animals: 	
	print "More people than animals"


animals += 5

if people < animals: 
	print "More animals than people"

print people == animals 

if people>animals:
	print "More people"
elif animals>people:
	print "More animals"
else: 
	print "Same nos"

if "good" == "bad": 
	print "good is bad"
else: 
	print "good is not bad"
"""

print "This is an adventure game"

door = raw_input("Please choose door 1 or 2: ")

if door == "1": 
	print "Jungle!! Make a choice"
	lion = raw_input("1 or 2: ")
	if lion == "1": 
		print "You got eaten! Sorry"
	elif lion == "2":
		print "You are safe"
	else: 
		print "Wrong choice"
elif door =="2":
	print "This is a theme park, go enjoy!"
else: 
	print "wrong choice"