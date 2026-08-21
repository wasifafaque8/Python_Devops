import sys

#more modular approach
def addition(num1,num2):
    add = num1+num2
    return add

def subtraction(num1,num2):
    sub= num1-num2
    return sub

x= print(addition(5,10))
y= print(subtraction(10,5))

num1= int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = addition(num1,num2)
    print(output)


