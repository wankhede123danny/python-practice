#Operators:
#Logical Operator
#If x evaluates to false return x otherwise return y (and)
x = 50 
y = 78
print(x and y)
n = 0.0      #(0,0.0,false,[],{},(),"",'')
m = 40
print(n and m)
e = ()
f= 10
print(e and f)
j=0.5
k= 78
print(j and k)
a =""
s = 34
print(a and s)
print("dn" and 'mn')

#If x evaluates to true then result x otherwise result is y (Or)
print(23 or 67)   #(0,0.0,false,[],{},(),"",'')
print(0 or 45)
print('ac' or 'cd')
print("" or "mn")
print(0 or 'ml')
print( "fg" or [])
print(() or "end")

#Logical operators
'''  T  F = F , T  T = T , F  F = F (AND)
     T  F = T , T  T = T , F  F = F (OR) '''
     
exp1 = 23>45
exp2 = 55>19
exp3 = 97>88
print("exp1 and exp2:", exp1 and exp2)
print("exp1 or exp2:", exp1 or exp2)
print("exp2 and exp3:", exp2 and exp3)


#Arithimatic operators
'''print("Addition of two number:",5+2)
print("sub of two number:",5-2)
print("Multification of two Numbers:",5*2)
print("Division of two number:",5/2); print("Div. of two numbers:",5//2)
print("moduluos of two number:",5%2)
print("Square of the number:",5**2)'''

add = 345+67+\
45.89+ 345+\
231.67;mul = 2*68*2; sub = 4567.56-2345-123
print(sub)
print(add)
print(mul)

#Other way to write multiline addition 
#we can use () instend of \ 
add =(345+67+45.89+ 
345+23.45+45+
231.67)
mul = 2*68*2 
sub = 4567.56-2345-123
print(sub)
print(add)
print(mul)

#Comparison operators
n1 = 34
n2 = 45
print(n1==n2)
print(n1!=n2)


#Augmented assignment:
a = 45
print(a)
a = a +10
print(a)

b = 45
print(b)
b += 10
print(b)
b -= 10
print(b)
b *= 5
print(b)
b /= 5
print(b)
b //= 5
print(b)
b **= 2
print(b)

#Membership Operator:
my_list = ["a","B","M",10]
print(my_list)
print("B" in my_list)
print("a" in my_list)
print('a' not in my_list)
print(10 in my_list)

#Ternary operator:
#<operand1> if <condition> else <operand2>
print("hii" if 10>5 else "bye")
print('hii' if 10<5 else 'bye')
result ="Hii" if 15>= 19 else "Bye"
print(result)

#Bitwise Operators:
#Walrus Operators:
