alphabets = ["a", "b", "c", "d", "e"]
numbers = [0, 1, 2, 3, 4]
boo = [True, False, True, True]
alpha_num = [1, "a", 2, "b"]

print alphabets
print numbers
print boo
print alpha_num


print "*********"

print alpha_num[0]
print alpha_num[1]

empty = []
print empty

print "list of alphabets"
for i in numbers:
	print "%d:  %s" %(numbers[i], alphabets[i])


print boo[0]==boo[1]
print boo[2]==boo[3]

for i in range(0,4):
	print "Element no %d is %r: " %(i+1, alpha_num[i])
	empty.append(alpha_num[i])

print "The empty list is now"
print empty  
