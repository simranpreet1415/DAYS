
#******loops******
# # conditional statements
# if statement 
a= 4
b= 3
if (a>b):
    print ("hello")


# # if else statement 
a= 4
b= 7
if (a>b):
    print ("hello")
else:
     print ("h")

a= 14
b=20
c=64
if (b>c):
   print ("H")
elif (a>c):
    print ("L")
elif (b==c):
    print ("R")
else:
    print ("LH")


# looping statements
for x in range (10):
    print(x)


for x in range (10):
     for y in range (11,15):
       print (x,y)


row = int(input("Enter number of rows: "))
print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()


# while loop
a=10
while (a<=100):
    print ("hello")  


# break    
num = 0
for i in range(10):
	num += 1
	if num == 8:
		break
	print("The num has value:", num)
print("Out of loop")

num = 0
for i in range(10):
	num += 1
	if num == 5:
		break
	print("The num has value:", num)
print("Out of loop")


# continue
# Python program to
# demonstrate continue
# statement


for i in range(1, 11):
	if i == 6:
		continue
	else:
		print(i, end=" ")



#******operators******
a= 14
b= 15
# # arithmetic operators
# # addition of two numbers
add = a+b
print (add)
# # subtraction of tewo numbers
sub = a-b
print (sub)
# # multiplication of two numbers 
mul = a*b
print (mul)
# # division of two numbers
div = a/b
print (div)
# # multiplication2 of two numbers
mul2 = a**b
print (mul2)
# # division2 of two numbers
div2 = a//b
print (div2)
# # modulus of two numbers
mod = a%b
print (mod)


# # relational operator
a = 4
b = 8
print (a<b)  
print (a>b)
print (a<=b)
print (a>=b)
print (a==b)
print (a!=b)

# # logical operators
a = 5
b = 15
print (a>b) and (b>a)
print (a<b) and (b>a)
print (a>b) or (b<a)
print (a<b) or (b>a)
print (a<b) or (b<a)
print (not(b>a))

# # assignment operator
a = 15
a+= 5
print (a)
a-= 5
print (a)
a*= 5
print (a)
a/= 5
print (a)
a**= 5
print (a)
a//= 5
print (a)
a%= 5
print (a)

# # bitwise operator
a=10
b=4
print (a&b)
print (a|b)
print (a^b)
print (a<<2)
print (a>>2)
print (~a)

# # identity operator
ab = 'python class'
print ('t' in ab) 
print ('t' not in ab) 


#******structures*****
for x in range(1, 5):
    for y in range(1, x+1):
         print("*", end="")
    print()


for x in range(5):
    for y in range(5-x):
         print("*", end="")
    print()

# square
row = int(input("Enter number of rows: "))
print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()


# pyramid
row = int(input('Enter number of rows required: '))
for i in range(row):
    for j in range(row-i):
        print(' ', end='') # printing space required and staying in same line
    
    for j in range(2*i+1):
        print('*',end='') # printing * and staying in same line
    print() # printing new line


