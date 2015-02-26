animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals [1] 

print animals[2] 

#animals[0] animals[3] animals[4] animals[2] animals[5] animals[4]

five_fruits = "Apples Oranges Grapes"
list_fruits = five_fruits.split(' ')
print list_fruits

ani = "bear, python, peacock, kangaroo, whale, platypus"
list_ani = ani.split(', ')
print list_ani
print list_ani[0]

print len(list_fruits)
while len(list_fruits)!=5: 
	a = list_ani.pop()
	list_fruits.append(a)

print "********************************************************************************************" 
print list_fruits
print list_fruits[-1]
list_fruits.pop()
print list_fruits[-1]

print ' '.join(list_fruits)
print '#'.join(list_fruits[0:3])
print list_fruits[0:3]