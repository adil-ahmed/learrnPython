#if-elif-else
max = 0
number1 = input("Please enter the first number: ")
number1 = int(number1)
number2 = input("Please enter the second number: ")
number2 = int(number2)
number3 = input("Please enter the third number: ")
number3 = int(number3)
if number1>number2 and number1>number3:
    max = number1
elif number2>number1 and number2>number3:
    max = number2
else:
    max = number3
print("Max(",number1,",",number2,",",number3,") =", max)

#leap year program
year =  input("Enter the year: ")
year = int(year)
if year%400 == 0:
    print(year,"is a leap year")
elif year%100 == 0:
    print(year,"is not a leap year")
elif year%4 == 0:
    print(year,"is a leap year")