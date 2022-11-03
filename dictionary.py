d = {}

type(d)

d = {"key":[1,2,3,4,5,(34,45)], "key1":(1,2,3,4,5),"key2":{'x':'sfs','y':'dfs'}}
print (d)

d['key2']['x']


for i in d:
    print(i)
    
    
for i in d:
    print(d[i])
    
    
d.keys()
d.values()


for i in d.keys():
    print(d[i])
    
    
a = []
for i in d.values():
    if type(i) == tuple:
            a.append(i)
            
            
dic_variable = {}

for i in range(10):
    dic_variable[i] = i **2
            
            
            
            
