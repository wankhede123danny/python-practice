
#Indexing
surname= 'wankhede' #01234567  #-8-7-6-5-4-3-2-1
print(surname[3])
print(surname[-3])
#Slicing
print(surname[1:7])     #surname[1:(7-1)
print(surname[-5:-2:])
print(surname[::])      #step bydafault value is 1
print(surname[::-1])    #reverse the string by step=1

#concatination operater (+)
a= "Dnyaneshwar"
b= "Wankhede"
print(a+"$$$"+b)
print(a+" "+b)

# repiter operator
a="hello"
print(a*5)
print(a*5,end=" ") # it dose not work
print(a*5,sep="---")

#Accessing
name = 'Dnyaneshwar'
for item in name:
    print(name)
#Escape Sequence:
print('dnyaneshwar\'s book')