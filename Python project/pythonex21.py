'''
namesphonenos = {'Paavni': 765865851, 'Aneesh': 5122179296}

print "The phone no for Paavni is %r" %(namesphonenos['Paavni'])

inforbook = {'Name': "Paavni", 'Phone': "7655865851", 'Age': 27, 'IsFemale': True}

print inforbook['IsFemale']

inforbook['IsStudent'] = True

print inforbook

del inforbook['Phone']

print inforbook
'''

states = {"California": "CA", "Washington": "WA", "Massachusetts": "MA"}
cities = {"CA": "Palo Alto", "WA": "Seattle", "MA": "Amherst"}

states["New York"] = "NY"
cities["NY"] = "New York"

print "*" *10 
print "Cities in WA: " ,cities["WA"]
print "Cities in California: " , cities[states["California"]]

print "*"* 10 
print "State and abbreviation"
for abbreviation, state in states.items(): 
	print state, ": ", abbreviation

print "*"* 10 
print "Cities and state"

for state, abbreviation in states.items(): 
	print state, ": ", abbreviation, "-->", cities[abbreviation]

state = states.get("Oregon")

if not state: 
	print "Oregon is not in the dictionary"

city = cities.get("OR", "NA")
print "cities listed for OR: ", city


