'''
print("hello")
number1 = 10
number2 = 11.4
number3 = "Good"

#printing
print(number1, number2, number3)

#checking types
print(type(number1))

#casting
a = 12
b = 15.5
result = a+b
print(result)

#Taking input
name = input("Enter your name: ")
print("Welcome dear", name)

#python automatically takes input as string
number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")
result = number1+number2
#Answer will be string: concating number1 & number2
print("Ans: ",result)
#We can convert it using int()
number1 = input("Enter number 1: ")
number1 = int(number1)
number2 = input("Enter number 2: ")
number2 = int(number2)
result = number1+number2
print("Ans: ",result)


#arithmetic operations
print("5+2 ",5+2)
print("5-2 ",5-2)
print("5*2 ",5*2)
print("5/2 ",5/2)
print("Division only integer part 5/2: ",5//2)
print("Square of 5: ",5**2)
print("5%2: ",5%2)
'''

#comparison operator
a = 50
b = 80
print("a==b", a==b)
print("a!=b", a!=b)
print("a>b", a>b)
print("a>=b", a>=b)
print("a<b", a<b)
print("a<=b", a<=b)
print("not(a==b)", not(a==b))

#Basic gates
x = 30
y = 60
print("x and y are even", x%2==0 and y%2==0)
print("y>70 or y<100", y>70 or y<100)