t1 = (1,3,4,6,7,8,9,'Aayush')
print(type(t1))

for i in range(len(t1)):
    print(i) 
    
# insert something at the 2nd element of the tuple
# tupples are im(mutable 

t1 = list(t1)
print(type(t1))
t1.insert(2,"Molu")

for i in t1:
    print (i)
    
t1 = tuple(t1)


for i in t1:
    print (i)
    #print (type(t1)) 
    
    
## SET 

set1 = set((11,11,22,22,45,12,11,56,96,42,232))

set2 = {1,3,4,5,6,6,1,3,4,5,6,7,8,9}


s3 = set2.union(set1)