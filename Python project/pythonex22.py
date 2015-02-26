import hashmap 
'''
#create a hasmap of states 
states = hashmap.new()

#set values 
hashmap.set(states, "Washington", "WA")
hashmap.set(states, "Oregon", "OR")
hashmap.set(states, "California", "CA")
hashmap.set(states, "Massachusetts", "MA")

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MA', 'Boston')
hashmap.set(cities, 'WA', 'Seattle')
hashmap.set(cities, 'CA', 'Palo ALto ')
hashmap.set(cities, 'MA', 'Amherst')

print "*" * 10
print "Cities"
print hashmap.get(cities, "MA")


print "-" *10
print "States with abbreviations"
print "Abbreviation for Washington is %s" % hashmap.get(states, "Washington")

print "#" * 10
print "Cities for states"
print "Cities for California are %s" % hashmap.get(cities, hashmap.get(states, "California"))

print "All states"
print hashmap.list(states)

print "New York"
state = hashmap.get(states, "NY")
if not state: 
	print ("No NY")
else: 
	print "Cities for NY are %s" % hashmap.get(cities, "NY", "NA")

'''
test = hashmap.new(2)
print test 

hashmap.set(test, "testkey1", "testvalue1")
hashmap.set(test, "testkey2", "testvalue2")
hashmap.set(test, "testkey3", "testvalue3")
print test[0]
print test[1]
