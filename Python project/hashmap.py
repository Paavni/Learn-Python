'''hashmap<-buckets<-slots<--(key, value)
hashmap is a collection of collection of key value slots 
'''
def new(num_buck = 256):
	aMap = [] #mepty list
	for i in range(0,num_buck):
		aMap.append([]) # list of lists 
						# appending empty list to list
	return aMap

def hash_key(aMap, key):
	return hash(key) % len (aMap) #modulus hash value by length of the list (no of buckets) to get a poistion 0, length-1 for the value of one of the buckets the key will go to 

def get_buck(aMap, key):
	buck_id = hash_key(aMap,key)
	return aMap[buck_id] # where is the key, the sam eway we find out weher to put the key?

def get_slot(aMap, key, default = None):
	bucket = get_buck(aMap,key)
	for i , kv in enumerate(bucket): #go over the bucket(list)
		k, v = kv #bucket[i] = kv = (k,v) 
		if key == k: #found matching key
			return i, k, v #return the index in the list, key and the value
	return -1, key, default # when key not found 

def get(aMap,key, default = None):
	i,k,v = get_slot(aMap, key, default = default)
	return v

def set(aMap, key, value):
	bucket = get_buck(aMap, key) #bucket 
	i, k, v = get_slot(aMap, key) #slot
	if i>=0:
		bucket[i] = (key, value)
	else:
		bucket.append((key,value))

def delete(aMap, key):
	bucket = get_buck(aMap, key) #get the bucket ID
	for i in xrange(len(bucket)): #go over the bucket 
		if key == k:
			del bucket[i]
			break #stop when key is found

#iterate over the bucket(list) in the aMap(list) and print the values
def list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v