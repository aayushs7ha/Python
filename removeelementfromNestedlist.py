# remove all 5 from the list

l = [4,5,6,7,[4,5,6,7,2],41,5,6,7,1]
for i in l:
    if i == (5):
        l.remove(5)
    if type(i) == list:
        for j in i:
            if j == 5:
                i.remove(j)
    print(l)
    
# remove 0  
l2 = [1,23,4,5,0,0,[0,0,7,1,2,2,6],0,6,7,8,0]
for i in l2:
    if i == 0:
        l2.remove(0)
    if type(i) == list:
        for j in i:
            if j == 0:
                i.remove(j)


l2      
            
            
    