#Dictionary:

#It does not allow duplicate keys
#In place of keys immutable(string,int,tuple etc) types are allowed
#Indexing is not apply on dictionary

d1 = {}      #empty dictionary
d2 = {"ram" : 345, "data":45, 1: "Raj",'value':[1,2,4,5], 5:"five",(3,): 8, (1,):"it's diff. type of key value than 1"}
d3 = dict()  #empty dictionary

'''print(type(d1),type(d2),type(d3))
print(d1,d2,d3)
print(len(d1),len(d2),len(d3))'''

'''print(d2[1])
#print(d2["shyam"])
#or
print(d2.get("shyam"))
print(d2.keys())
print(d2.values())
print(d2.items())
d2.update({"wankhede":"surname","danny":"name", 4 :"four", "data": 95})
print(d2)
del d2["value"]
print(d2)'''

'''#Comprehension:
a = [x for x in range(10)] #list
b = {x for x in range(20,31)} #set

d = { k:v for k , v in zip (a,b)} 
print(d)

import string
alpha = string.ascii_uppercase
num = range(26)
d5 = {keys:values for keys,values in zip (num,alpha)}
print(d5)'''

#Dictionary:
# profile = {'name':"dnyaneshwar",'agr':29,'hobby':'coding'}      
# print(profile)    


l = []
print(l)

for i in range(10):
    result = 4+i
    l.append(result)
    print(l)

# print(l)
# if len(l) > 0:
#     print("operation completed")
    
