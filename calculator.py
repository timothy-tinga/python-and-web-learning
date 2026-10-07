num1=int(input("Enter your first number> "))
num2=int(input("Enter yuor second number> "))

print("1: Multiplication is")
print("2: Division is")
print("3: Addition is")
print("4: Subtraction is")
print("5: modulus")

choice=input("Enter your choice> ")

def mult(y,z):
    print("multplication is", y * z)
if choice=="1":
    mult(num1, num2)

def div(y,z):
    print("Division is", y/z)
if choice=="2":
    div(num1,num2)

def Add(y,z):
    print("The sum is", y+z)
if choice=="3":
    Add(num1,num2)

def mod(z,y):
    print("modulus is",y%z)
if choice=="5":
    mod(num1,num2)

def sub(y,z):
    print("Your diference is", y-z )
if choice=="4":
    sub(num1,num2)
